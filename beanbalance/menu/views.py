from django.shortcuts import render, redirect,get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from django.views import View
from django.utils import timezone

from menu.models import Menu, Category
from order.models import Order, OrderMenu, Payment
from django.contrib.auth.models import User
from menu.forms import CategoryForm, MenuForm


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

class MenuManageView(View):
    template_name = "manage.html"
    
    def get(self, request):
        add_category_form = CategoryForm()
        add_menu_form = MenuForm()
        categories = Category.objects.all()
        menus = Menu.objects.all()

        context = {
            "add_category_form": add_category_form,
            "add_menu_form": add_menu_form,
            "categories": categories,
            "menus": menus,
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form_type = request.POST.get('form_type')

        add_category_form = CategoryForm()
        add_menu_form = MenuForm()

        if form_type == 'category':
            add_category_form = CategoryForm(request.POST)
            if add_category_form.is_valid():
                add_category_form.save()
                return redirect('manage')
        elif form_type == 'menu':
            add_menu_form = MenuForm(request.POST)
            if add_menu_form.is_valid():
                add_menu_form.save()
                return redirect('manage')
        
        # Ensure forms are re-rendered with errors if validation fails
        categories = Category.objects.all()
        menus = Menu.objects.all()
        return render(request, self.template_name, {
            "add_category_form": add_category_form,
            "add_menu_form": add_menu_form,
            "categories": categories,
            "menus": menus
        })

    
class editMenuView(View):
    def put(self, request, menu_id):
        try:
            body = json.loads(request.body)
            menu_item = get_object_or_404(Menu, id=menu_id)
            
            menu_item.name = body.get('name')
            menu_item.description = body.get('description')
            menu_item.price = body.get('price')
            menu_item.category_id = body.get('category')

            menu_item.save()

            return JsonResponse({'message': 'Menu updated successfully'})
        
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
        
class MenuDeleteView(View):
    def delete(self, request, menu_id):
        try:
            menu_item = get_object_or_404(Menu, id=menu_id)
            menu_item.delete()
            return JsonResponse({'message': 'Menu item deleted successfully'})
        
        except Exception as e:
            # Return an error response with the exception message
            return JsonResponse({'error': str(e)}, status=500)