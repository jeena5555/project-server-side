from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('', views.EmployeeView.as_view(), name='employee'),  # Listing and adding employees
    path('update/<int:employee_id>/', views.EmployeeUpdateView.as_view(), name='employee_update'),  # Update an employee
    path('delete/<int:employee_id>/', views.EmployeeDeleteView.as_view(), name='employee_delete'),  # Delete an employee
    path('password_change/', views.ChangePasswordView.as_view(),name='password_change'),
]
