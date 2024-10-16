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
    permission_required = ["order.view_payment", "order.add_payment"]

    template_name = "payment.html"
    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        data = json.loads(request.body)
        cart = data.get('cart')
        total = data.get('total')
        payment_method = data.get('payment_method')

        employee = request.user

        # Create an order
        order = Order.objects.create(
            amount=total,
            order_date=timezone.localtime().date(),
            order_time=timezone.localtime().time(),
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
            add_category_form = CategoryForm(request.POST)
            add_menu_form = MenuForm()
            if add_category_form.is_valid():
                # Process category form
                add_category_form.save()
                return redirect('manage')

        elif 'menu_submit_button' in request.POST:
            add_category_form = CategoryForm()
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
            name = body.get('name')
            price = body.get('price')
            description = body.get('description')
            category_id = body.get('category')

            errors = {}

            # Validate if all fields are present
            if not name:
                errors['name'] = 'Name is required.'
            if not price:
                errors['price'] = 'Price is required.'
            if not description:
                errors['description'] = 'Description is required.'
            if not category_id:
                errors['category'] = 'Category is required.'

            # Validate category (assuming it's a foreign key)
            if category_id and not Category.objects.filter(id=category_id).exists():
                errors['category'] = 'Category does not exist.'

            # Ensure the menu name is unique, excluding the current menu item
            if Menu.objects.filter(name=name).exclude(id=menu_id).exists():
                errors['name'] = 'Menu name already exists.'

            # Validate price (ensure it's a valid float and greater than 0)
            if price:
                try:
                    price = float(price)
                    if price <= 0:
                        errors['price'] = 'Menu price must be greater than 0.'
                except ValueError:
                    errors['price'] = 'Invalid price value.'

            # If there are any errors, return them
            if errors:
                return JsonResponse({'errors': errors}, status=400)

            # Get the menu item by ID and update it
            menu_item = get_object_or_404(Menu, id=menu_id)
            menu_item.name = name
            menu_item.description = description
            menu_item.price = price
            menu_item.category_id = category_id

            # Save updated menu item
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
            return JsonResponse({'error': str(e)}, status=500)

class CategoryUpdateView(LoginRequiredMixin, PermissionRequiredMixin,View):
    login_url = "/authen/"
    permission_required = ["menu.change_category"]
    def put(self, request, category_id):
        try:
            body = json.loads(request.body)
            new_category_name = body.get('name')

            # Check if the new category name is empty
            if not new_category_name:
                return JsonResponse({'error_message': 'Category name cannot be empty'}, status=400)

            # Check if the new category name already exists, excluding the current category
            if Category.objects.filter(name=new_category_name).exclude(id=category_id).exists():
                return JsonResponse({'error_message': 'Category name already exists'}, status=400)

            # Get the category by ID
            category = get_object_or_404(Category, id=category_id)

            # Update the category name and save
            category.name = new_category_name
            category.save()

            # Return a success message
            return JsonResponse({'message': 'Category updated successfully'}, status=200)

        except json.JSONDecodeError:
            return JsonResponse({'error_message': 'Invalid JSON format'}, status=400)

        except Category.DoesNotExist:
            return JsonResponse({'error_message': 'Category not found'}, status=404)

        except Exception as e:
            # Return a generic error message
            return JsonResponse({'error_message': str(e)}, status=500)



class CategoryDeleteView(LoginRequiredMixin, PermissionRequiredMixin,View):
    login_url = "/authen/"
    permission_required = ["menu.delete_category"]
    def delete(self, request, category_id):
        try:
            category = get_object_or_404(Category, id=category_id)
            category.delete()
            return JsonResponse({'message': 'Category deleted successfully'})

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
