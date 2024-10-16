from django import forms
from django.forms import modelformset_factory

from employees.models import Employee
from schedule.models import Schedule

class FilterEmployeeForm(forms.Form):
    ALL_CHOICE = [("ALL", "All Employees")]  # Add this choice for "ALL"

    # Fetch employees and add the ALL_CHOICE at the start
    select = forms.ChoiceField(
        choices=ALL_CHOICE + list(Employee.objects.values_list('id', 'first_name')),
        label="Filter Employee",
        widget=forms.Select(attrs={
            'class': 'w-24 p-2 border rounded'
        }),
    )

class ScheduleForm(forms.ModelForm):
    employee = forms.ModelChoiceField(
        queryset=Employee.objects.all(),
        widget=forms.Select(attrs={
            'class': 'w-24 p-2 border rounded'
        })
    )

    date=forms.DateField(
        widget=forms.DateInput(attrs={
            'type': 'date',
            'class': 'w-30 p-2 border rounded',
            'readonly': 'readonly'
        }),
    )

    status=forms.ChoiceField(
        choices=Schedule.Status.choices,
        widget=forms.Select(attrs={
            'class': 'w-24 p-2 border rounded'
        }),
    )

    class Meta:
        model = Schedule
        fields = ['employee', 'date', 'status']
