from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from django.views import View
from menu.models import Menu, Category
from order.models import Order

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
        # Load data from the request body
        data = json.loads(request.body)

        # Render the template with the received data
        return render(request, self.template_name, {'cart': data})



