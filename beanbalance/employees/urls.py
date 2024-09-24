from django.urls import path

from employees.views import EmployeeView

urlpatterns = [
    path('', EmployeeView.as_view(), name="employee")
]
