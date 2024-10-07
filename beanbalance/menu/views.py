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
            "categories" : categories,
            "menus" : menus,
        }
        return render(request, self.template_name, context)
    
    def post(self, request):
        form_type = request.POST.get('form_type')

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
        return render(request, self.template_name, {"add_category_form": add_category_form, "add_menu_form": add_menu_form})  # Re-render the form with errors if invalid
    
class editMenuView(View):
    template_name = "manage.html"

    def get(self, request):
        menu_id = request.GET.get('id')
        if menu_id:
            try:
                menu_item = Menu.objects.get(pk=menu_id)
                form = MenuForm(instance=menu_item)  # Pre-fill the form with menu data
                return render(request, self.template_name, {'form': form, 'menu_id': menu_id})
            except Menu.DoesNotExist:
                return JsonResponse({'error': 'Menu item not found.'}, status=404)
        return JsonResponse({'error': 'Menu ID not provided.'}, status=400)

    # def post(self, request):
    #     menu_id = request.POST.get('id')
    #     if menu_id:
    #         menu_item = get_object_or_404(Menu, pk=menu_id)
    #         form = MenuForm(request.POST, instance=menu_item)
    #         if form.is_valid():
    #             form.save()  # Save the updated menu item
    #             return JsonResponse({'message': 'Menu item updated successfully.'})
    #         else:
    #             # Form is not valid, send errors
    #             return render(request, self.template_name, {'form': form, 'menu_id': menu_id})
    #     return JsonResponse({'error': 'Invalid menu ID or data.'}, status=400)