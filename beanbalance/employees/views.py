from django.shortcuts import render, redirect
from django.views import View
from .models import Employee
from employees.forms import AddEmployeeForm
from django.contrib.auth.models import User
from django.db import transaction


# Create your views here.


class EmployeeView(View):
    template_name = 'employees.html'

    def get(self, request):
        employees = User.objects.all()
        return render(request, self.template_name, {"employees": employees})

class EmployeeManageView(View):
    def get(self, request):
        employees = Employee.objects.all()  # Get all employee data
        context = {"employees": employees}  # Change the key to be plural and more descriptive
        return render(request, 'employee_manage.html', context)

class EmployeeAddView(View):
    def get(self, request):
        form = AddEmployeeForm()
        return render(request, "employee_add_employee.html", {"form": form})

    def add_employee(request):
        if request.method == "POST":
            form = AddEmployeeForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('employee_list')  # Redirect to a list or another relevant page
        else:
            form = AddEmployeeForm()

        return render(request, 'add_employee.html', {'form': form})

