from django.urls import path
from inventory import views

urlpatterns = [
    path('', views.InventoryView.as_view(), name='inventory'),
    path('update/<int:item_id>/', views.InventoryUpdateView.as_view(), name='update_inventory'),
    path('delete/<int:item_id>/', views.InventoryDeleteView.as_view(), name='delete_inventory'),  # Optional delete
]
