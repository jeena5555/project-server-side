from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.views import View
from .models import Employee
from employees.forms import AddEmployeeForm
import json
from django.db import transaction

# Employee View to manage listing and adding employees
class EmployeeView(View):
    template_name = 'employee_manage.html'

    def get(self, request):
        # Display the employee list
        employees = Employee.objects.all()
        form = AddEmployeeForm()
        return render(request, self.template_name, {"employees": employees, "form": form})

    def post(self, request):
        # Add a new employee
        form = AddEmployeeForm(request.POST)
        if form.is_valid():
            with transaction.atomic():
                form.save()
            return redirect('employee_manage')  # Redirect to the employee list after adding a new item
        # If form is not valid, re-render the page with errors
        employees = Employee.objects.all()
        return render(request, self.template_name, {"employees": employees, "form": form})

# Update employee view
class EmployeeUpdateView(View):
    def put(self, request, employee_id):
        try:
            body = json.loads(request.body)
            employee = get_object_or_404(Employee, id=employee_id)
            employee.first_name = body.get('first_name', employee.first_name)
            employee.last_name = body.get('last_name', employee.last_name)
            employee.gender = body.get('gender', employee.gender)
            employee.birth_date = body.get('birth_date', employee.birth_date)
            employee.position = body.get('position', employee.position)
            employee.save()
            return JsonResponse({'message': 'Employee updated successfully'})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

# Delete employee view
class EmployeeDeleteView(View):
    def delete(self, request, employee_id):
        try:
            employee = get_object_or_404(Employee, id=employee_id)
            employee.delete()
            return JsonResponse({'message': 'Employee deleted successfully'})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
