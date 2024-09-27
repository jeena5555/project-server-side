from django.shortcuts import render
from django.views import View

from django.contrib.auth.models import User

# Create your views here.


class EmployeeView(View):
    template_name = 'employees.html'

    def get(self, request):
        employees = User.objects.all()

        return render(request, self.template_name, {"employees": employees})

class EmployeeManageView(View):
    def get(self, request):
        return render(request, 'employee_manage.html')

class EmployeeAddView(View):
    def get(self, request):
        return render(request, 'employee_add_position.html')
