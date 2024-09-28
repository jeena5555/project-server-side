from django.shortcuts import render
from django.views import View
from order.models import Order, OrderMenu
from order.forms import DateFilterForm

# Create your views here.

class OrderHistoryView(View):
    template_name = "order_history.html"

    def get(self, request):
        form = DateFilterForm(request.GET)
        orders = Order.objects.all()

        if form.is_valid() and form.cleaned_data['order_date']:
            selected_date = form.cleaned_data.get('order_date')
            # Filter orders by the selected date (assuming you have a 'created_at' or similar date field)
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
