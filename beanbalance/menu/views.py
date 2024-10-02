from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from django.views import View
from django.utils import timezone

from menu.models import Menu, Category
from order.models import Order, OrderMenu, Payment
from django.contrib.auth.models import User


import json

# Create your views here.

class MenuView(View):
    template_name = "menu.html"

    def get(self, request):
        menus = Menu.objects.all()
        categories = Category.objects.all()

        selected_category = request.GET.get('category', 'ALL')

        if selected_category == 'ALL':
            menus = Menu.objects.all()
        else:
            menus = Menu.objects.filter(category__name=selected_category)
        context = {
            "menus": menus,
            "categories": categories,
            "selected_category": selected_category
        }
        return render(request, self.template_name, context)

class PaymentView(View):
    template_name = "payment.html"
    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        data = json.loads(request.body)
        cart = data.get('cart')
        total = data.get('total')
        payment_method = data.get('payment_method')

        employee = User.objects.get(id=1)

        # Create an order
        order = Order.objects.create(
            amount=total,
            order_date=timezone.now().date(),
            order_time=timezone.now().time(),
            employee=employee
        )

        # Create OrderMenu entries for each menu item in the cart
        for item in cart:
            menu = Menu.objects.get(id=item['id'])  # Assuming the menu ID is passed in the cart
            quantity = item['quantity']  # Quantity of the menu item
            OrderMenu.objects.create(
                order=order,
                menu=menu,
                quantity=quantity
                )

        # Create a payment record for the order
        Payment.objects.create(
            order=order,
            amount=total,
            payment_method=payment_method,
            payment_date=timezone.now().date(),
            payment_time=timezone.now().time()
        )

        return JsonResponse({'status': 'success', 'order_id': order.id})




