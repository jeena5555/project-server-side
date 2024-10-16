# views.py

from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from django.utils import timezone
from order.models import Order, OrderMenu
from order.forms import DateFilterForm

class OrderHistoryView(LoginRequiredMixin, PermissionRequiredMixin, View):
    login_url = "/authen/"
    permission_required = ["order.view_order"]

    template_name = "order_history.html"

    def get(self, request):
        today = timezone.localtime().date()

        form = DateFilterForm(request.GET or {'order_date': today})

        orders = Order.objects.all()

        if form.is_valid():
            selected_date = form.cleaned_data.get('order_date')
            if selected_date:
                orders = orders.filter(order_date=selected_date)

        orders_with_menus = []
        for order in orders:
            order_menus = OrderMenu.objects.filter(order_id=order.id)
            orders_with_menus.append({
                'order': order,
                'order_menus': order_menus
            })

        context = {
            "orders": orders_with_menus,
            "form": form
        }
        return render(request, self.template_name, context)
