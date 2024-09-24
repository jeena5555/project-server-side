from django.urls import path

from employees.views import EmployeeView, SidebarView

urlpatterns = [
    path('', EmployeeView.as_view(), name="employee"),
    path('test', SidebarView.as_view(), name="test"),
]
