from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from dashboard.forms import SelectSalesTrendsForm, GenerateReportForm
from order.models import Order, OrderMenu
from menu.models import Menu
import json

from django.utils import timezone
from datetime import datetime, timedelta
from django.db.models import Sum
from django.utils.timezone import now
from datetime import date
from django.db.models.functions import TruncHour



class DashboardView(LoginRequiredMixin, View):
    login_url = "/authen/"

    template_name = "dashboard_date.html"

    def get(self, request):
        today = timezone.localtime().date()

        form = GenerateReportForm(request.GET or {'date': today})

        if form.is_valid():
            selected_date = form.cleaned_data.get('date')

            peek_time = self.peek_time(selected_date)
            top_selling_items = self.get_top_selling_items(selected_date)
            total_amount = self.total_sales_amount(selected_date)
            order_sales = self.order_sales(selected_date)
            average_order_value = self.average_order_value(selected_date)
            graph, labels = self.graph(selected_date)


        context = {
            'form': form,
            'peek_time': peek_time,
            'top_selling': top_selling_items,
            'total_amount': total_amount,
            'order_sales': order_sales,
            'average_order_value': average_order_value,
            'graph_data': graph,
            'graph_labels': labels,
        }
        return render(request, self.template_name, context)

    def peek_time(self, date=None):
        if date is None:
            date = now().date()

        orders_by_time = (
        Order.objects
        .filter(order_date=date)
        .annotate(hour=TruncHour('order_time'))
        .values('hour')
        .annotate(total_sales=Sum('amount'))
        .order_by('-total_sales')
        )

        if orders_by_time.exists():
            peek_time = orders_by_time.first()['hour']
            return peek_time
        else:
            return None

    def total_sales_amount(self, date=None):
        # If no date is provided, use today's date
        if date is None:
            date = now().date()
        total_amount = Order.objects.filter(order_date=date).aggregate(Sum('amount'))['amount__sum'] or 0
        return total_amount

    def order_sales(self, date=None):
        if date is None:
            date = now().date()
        order_sales = Order.objects.filter(order_date=date).count()
        return order_sales

    def average_order_value(self, date=None):
        if date is None:
            date = now().date()
        total_amount = Order.objects.filter(order_date=date).aggregate(Sum('amount'))['amount__sum'] or 0
        order_count = Order.objects.filter(order_date=date).count() or 1 
        average_order_value = total_amount / order_count
        return round(average_order_value, 2)

    def get_top_selling_items(self, date=None):
        if date is None:
            date = now().date()
        top_selling_menu = (
            OrderMenu.objects
            .filter(order__order_date=date)
            .values('menu')
            .annotate(total_quantity=Sum('quantity'))
            .order_by('-total_quantity')[:10]
        )

        top_selling_items = []
        for item in top_selling_menu:
            menu_item = Menu.objects.get(id=item['menu'])
            top_selling_items.append({
                'menu_item': menu_item,
                'total_quantity': item['total_quantity'],
            })
        return top_selling_items

    def graph(self, date=None):
        labels = []
        graph_data = []

        if date is None:
            date = now().date()
        labels = ['10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00', '17:00', '18:00']
        for hour in range(10, 19):
            start_time = datetime.combine(date, datetime.min.time()).replace(hour=hour)
            end_time = start_time + timedelta(hours=1)

            total_amount = Order.objects.filter(
                order_date=date,
                order_time__gte=start_time.time(),
                order_time__lt=end_time.time()
            ).aggregate(Sum('amount'))['amount__sum'] or 0

            graph_data.append(float(total_amount))

        return graph_data, labels


class DashboardAllView(LoginRequiredMixin, View):
    login_url = "/authen/"

    template_name = 'dashboard_all.html'

    def get(self, request):
        form = SelectSalesTrendsForm(request.GET or {'select': 'week'})
        graph_data = []
        labels = []

        if form.is_valid():
            selected_value = form.cleaned_data['select']
            current_time = now().date()

            graph_data, labels = self.aggregate_data(selected_value, current_time)

            labels_json = json.dumps(labels)
            graph_data_json = json.dumps(graph_data)

            peek_time = self.peek_time()
            top_selling_items = self.get_top_selling_items()
            total_amount = self.total_sales_amount()
            order_sales = self.order_sales()
            average_order_value = self.average_order_value()

            return render(request, self.template_name, {
                "form": form,
                "labels": labels_json,
                "graph_data": graph_data_json,
                'peek_time': peek_time,
                'top_selling': top_selling_items,
                'total_amount': total_amount,
                'order_sales': order_sales,
                'average_order_value': average_order_value,
            })

    def peek_time(self):
        orders_by_time = (
        Order.objects
        .annotate(hour=TruncHour('order_time'))
        .values('hour')
        .annotate(total_sales=Sum('amount'))
        .order_by('-total_sales')
        )

        peek_time = orders_by_time.first()['hour']
        return peek_time

    def total_sales_amount(self):
        total_amount = Order.objects.aggregate(Sum('amount'))['amount__sum'] or 0
        return total_amount

    def order_sales(self):
        order_sales = Order.objects.count()
        return order_sales

    def average_order_value(self):
        total_amount = Order.objects.aggregate(Sum('amount'))['amount__sum'] or 0
        order_count = Order.objects.count() or 1  # Avoid division by zero
        average_order_value = total_amount / order_count
        return round(average_order_value,2)

    def get_top_selling_items(self):
        top_selling_menu = (
            OrderMenu.objects
            .values('menu')
            .annotate(total_quantity=Sum('quantity'))
            .order_by('-total_quantity')[:10]
        )

        top_selling_items = []
        for item in top_selling_menu:
            menu_item = Menu.objects.get(id=item['menu'])
            top_selling_items.append({
                'menu_item': menu_item,
                'total_quantity': item['total_quantity'],
            })
        return top_selling_items

    def aggregate_data(self, selected_value, current_time):
        labels = []
        graph_data = []

        if selected_value == 'week':
            start_date = current_time - timedelta(days=current_time.weekday())
            labels = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

            for i in range(7):
                day = start_date + timedelta(days=i)
                total_amount = Order.objects.filter(order_date=day).aggregate(Sum('amount'))['amount__sum'] or 0
                graph_data.append(float(total_amount))

        elif selected_value == 'month':
            start_date = current_time.replace(day=1)
            labels = ['Week 1', 'Week 2', 'Week 3', 'Week 4']

            for i in range(4):
                week_start = start_date + timedelta(weeks=i)
                week_end = week_start + timedelta(weeks=1)
                total_amount = Order.objects.filter(
                    order_date__gte=week_start,
                    order_date__lt=week_end
                ).aggregate(Sum('amount'))['amount__sum'] or 0
                graph_data.append(float(total_amount))

        elif selected_value == 'year':
            start_date = current_time.replace(month=1, day=1)
            labels = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

            for month in range(1, 13):
                month_start = start_date.replace(month=month)
                month_end = (month_start + timedelta(days=32)).replace(day=1) - timedelta(days=1)
                total_amount = Order.objects.filter(
                    order_date__gte=month_start,
                    order_date__lt=month_end
                ).aggregate(Sum('amount'))['amount__sum'] or 0
                graph_data.append(float(total_amount))

        return graph_data, labels
