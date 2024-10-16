from django.shortcuts import render, redirect,get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from django.views import View
from django.utils import timezone

from menu.models import Menu, Category
from order.models import Order, OrderMenu, Payment
from django.contrib.auth.models import User
from menu.forms import CategoryForm, MenuForm



import json

# Create your views here.

class MenuView(LoginRequiredMixin, PermissionRequiredMixin,View):
    login_url = "/authen/"
    permission_required = ["menu.view_menu"]
    
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

class PaymentView(LoginRequiredMixin, PermissionRequiredMixin, View):
    login_url = "/authen/"
    permission_required = ["payment.view_payment"]
    
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

class MenuManageView(LoginRequiredMixin, PermissionRequiredMixin,View):
    login_url = "/authen/"
    permission_required = ["menu.view_menu", "menu.add_menu"]
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
        if 'category_submit_button' in request.POST:
            # Initialize only the category form with POST data, and menu form as an empty form
            add_category_form = CategoryForm(request.POST)
            add_menu_form = MenuForm()  # Empty form, not processed
            if add_category_form.is_valid():
                # Process category form
                add_category_form.save()
                return redirect('manage')
        elif 'menu_submit_button' in request.POST:
            # Initialize only the menu form with POST data, and category form as an empty form
            add_category_form = CategoryForm()  # Empty form, not processed
            add_menu_form = MenuForm(request.POST)
            if add_menu_form.is_valid():
                # Process menu form
                add_menu_form.save()
                return redirect('manage')
        
        categories = Category.objects.all()
        menus = Menu.objects.all()
        
        context = {
            "add_category_form": add_category_form,
            "add_menu_form": add_menu_form,
            "categories": categories,
            "menus": menus
        }
        return render(request, self.template_name, context)

class editMenuView(LoginRequiredMixin, PermissionRequiredMixin,View):
    login_url = "/authen/"
    permission_required = ["menu.change_menu"]
    def put(self, request, menu_id):
        try:
            body = json.loads(request.body)
            print('Request Body:', body)  # ตรวจสอบว่าข้อมูลที่ถูกส่งเข้ามาคืออะไร
            name = body.get('name')
            price = body.get('price')
            description = body.get('description')
            category = body.get('category')
            
             # Validate if all fields are present
            if not all([name, price, description, category]):
                return JsonResponse({'error': 'Missing fields in request'}, status=400)
            # Validate category (assuming it's a foreign key)
            if not Category.objects.filter(id=category).exists():
                return JsonResponse({'error_message': 'Category does not exist'}, status=400)
            # try:
            #     category = int(category)  # Convert category to integer
            # except ValueError:
            #     return JsonResponse({'error_message': 'Invalid category value'}, status=400)
            if not Category.objects.filter(id=category).exists():
                return JsonResponse({'error_message': 'Category does not exist'}, status=400)
            if Menu.objects.filter(name=name).exclude(id=menu_id).exists():
                return JsonResponse({'error': 'Menu name already exists'}, status=400)
            if price is not None and float(price) <= 0:
                return JsonResponse({'error': 'Menu price must be greater than 0'}, status=400)
            
            menu_item = get_object_or_404(Menu, id=menu_id)
            menu_item.name = name
            menu_item.description = description
            menu_item.price = price
            menu_item.category_id = category

            menu_item.save()

            return JsonResponse({'message': 'Menu updated successfully'})
        
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
        
class MenuDeleteView(LoginRequiredMixin, PermissionRequiredMixin,View):
    login_url = "/authen/"
    permission_required = ["menu.delete_menu"]
    def delete(self, request, menu_id):
        try:
            menu_item = get_object_or_404(Menu, id=menu_id)
            menu_item.delete()
            return JsonResponse({'message': 'Menu item deleted successfully'})
        
        except Exception as e:
            # Return an error response with the exception message
            return JsonResponse({'error': str(e)}, status=500)

class CategoryUpdateView(LoginRequiredMixin, PermissionRequiredMixin,View):
    login_url = "/authen/"
    permission_required = ["category.change_category"]
    def put(self, request, category_id):
        try:
            body = json.loads(request.body)
            new_category_name = body.get('name')
            
            if Category.objects.filter(name=new_category_name).exclude(id=category_id).exists():
                return JsonResponse({'error_message': 'Category name already exists'}, status=400)

            category = get_object_or_404(Category, id=category_id)
            # Update category name
            category.name = new_category_name
            category.save()

            return JsonResponse({'message': 'Category updated successfully'})
        
        except Exception as e:
            # Return a JSON response with the error message
            return JsonResponse({'error_message': str(e)}, status=500)


        
class CategoryDeleteView(LoginRequiredMixin, PermissionRequiredMixin,View):
    login_url = "/authen/"
    permission_required = ["category.delete_category"]
    def delete(self, request, category_id):
        try:
            category = get_object_or_404(Category, id=category_id)
            category.delete()
            return JsonResponse({'message': 'Category deleted successfully'})

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)