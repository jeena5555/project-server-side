from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views import View
from .models import Category
from inventory.forms import CategoryForm
import json

# Inventory View to manage listing and adding categories
class InventoryView(LoginRequiredMixin, PermissionRequiredMixin,View):
    login_url = "/authen/"
    permission_required = ["inventory.view_category", "inventory.add_category"]
    template_name = 'inventory_manage.html'

    def get(self, request):
        # Display the inventory list
        inventory = Category.objects.all().order_by('quantity')
        form = CategoryForm()
        return render(request, self.template_name, {"inventory": inventory, "form": form})
    
    def post(self, request):
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})  # ส่ง response เมื่อฟอร์มสำเร็จ
        else:
            # ส่งข้อผิดพลาดของฟอร์มกลับไปในรูปแบบ JSON
            return JsonResponse({'success': False, 'errors': form.errors})

# Update inventory view
class InventoryUpdateView(LoginRequiredMixin, PermissionRequiredMixin,View):
    login_url = "/authen/"
    permission_required = ["inventory.change_category"]
    def put(self, request, item_id):
        try:
            body = json.loads(request.body)
            item = get_object_or_404(Category, id=item_id)
            item.name = body.get('name', item.name)
            item.price = body.get('price', item.price)
            item.quantity = body.get('quantity', item.quantity)
            item.save()
            return JsonResponse({'message': 'Item updated successfully'})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

# Note: If needed, you can also add delete functionality in a similar way:
class InventoryDeleteView(LoginRequiredMixin, PermissionRequiredMixin,View):
    login_url = "/authen/"
    permission_required = ["inventory.delete_category"]
    def delete(self, request, item_id):
        try:
            item = get_object_or_404(Category, id=item_id)
            item.delete()
            return JsonResponse({'message': 'Item deleted successfully'})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
