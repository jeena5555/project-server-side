from django.urls import path

from employees.views import EmployeeView, EmployeeManageView,EmployeeAddView

urlpatterns = [
    path('', EmployeeView.as_view(), name="employee"),
    path('edit', EmployeeManageView.as_view(), name="edit-employee"),
    path('edit/add-employee', EmployeeAddView.as_view(), name="add-employee"),
]
