from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.views import View
from .models import Employee
from django.contrib.auth.models import Group
from employees.forms import AddEmployeeForm
import json
from django.db import transaction

from django.contrib.auth import logout
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
# Employee View to manage listing and adding employees
class EmployeeView(View):
    template_name = 'employee_manage.html'

    def get(self, request):
        employees = Employee.objects.all()
        employee_positions = []
        for employee in employees:
            position = Group.user_set.through.objects.get(user_id=employee.account.id)
            employee_positions.append({"employee": employee, "position": position})

        form = AddEmployeeForm()
        return render(request, self.template_name, {"employee_positions": employee_positions, "form": form})

    def post(self, request):
        # Add a new employee
        form = AddEmployeeForm(request.POST)
        if form.is_valid():
            with transaction.atomic():
                form.save()
            return redirect('employee')  # Redirect to the employee list after adding a new item
        # If form is not valid, re-render the page with errors
        employees = Employee.objects.all()
        return render(request, self.template_name, {"employees": employees, "form": form})

# Update employee view
class EmployeeUpdateView(View):
    def put(self, request, employee_id):
        try:
            body = json.loads(request.body)  # Parse JSON request body
            employee = get_object_or_404(Employee, id=employee_id)  # Fetch employee by ID

            # Update employee fields
            employee.first_name = body.get('first_name', employee.first_name)
            employee.last_name = body.get('last_name', employee.last_name)
            employee.gender = body.get('gender', employee.gender)
            employee.birth_date = body.get('birth_date', employee.birth_date)
            employee.salary = body.get('salary', employee.salary)

            # Update position (Group)
            if body.get('position'):
                group = Group.objects.get(name=body.get('position'))
                employee.account.groups.clear()
                employee.account.groups.add(group)

            # Update the User account (optional)
            if body.get('account'):
                employee.account.username = body.get('account')

            # Update password if it's provided (and different from default)
            if body.get('password') and body['password'] != '********':
                employee.account.set_password(body['password'])  # Set new password
                employee.account.save()  # Save account changes

            employee.save()  # Save employee changes

            return JsonResponse({'message': 'Employee updated successfully'})  # Success message

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)  # Error response
            return JsonResponse({'error': str(e)}, status=500)

class EmployeeDeleteView(View):
    def delete(self, request, employee_id):
        try:
            # Get the employee object or return a 404 if not found
            employee = get_object_or_404(Employee, id=employee_id)
            user = employee.account 

            # Delete the employee and the associated User account
            employee.delete()
            user.delete()

            return JsonResponse({'message': 'Employee deleted successfully'})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

class ChangePasswordView(PasswordChangeView):
    template_name = 'password_change.html'
    success_url = reverse_lazy('login')  # Redirect to the login page after logout

    def form_valid(self, form):
        # Change the password
        response = super().form_valid(form)
        # Log out the user
        logout(self.request)
        # Redirect to the login page
        return redirect(self.success_url)
