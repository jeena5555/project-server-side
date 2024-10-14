from django import forms
from .models import Employee
from django.contrib.auth.models import User, Group
from datetime import date

class AddEmployeeForm(forms.ModelForm):
    # Define each field with widgets and attributes for styling
    first_name = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={
            'placeholder': 'First Name',
            'class': 'w-full p-2 mb-4 border rounded'
        })
    )

    last_name = forms.CharField(
        max_length=200,
        widget=forms.TextInput(attrs={
            'placeholder': 'Last Name',
            'class': 'w-full p-2 mb-4 border rounded'
        })
    )
    
    gender = forms.ChoiceField(
        choices=Employee.Gender.choices,
        widget=forms.Select(attrs={
            'class': 'w-full p-2 mb-4 border rounded'
        })
    )
    
    birth_date = forms.DateField(
        widget=forms.DateInput(attrs={
            'type': 'date',
            'class': 'w-full p-2 mb-4 border rounded'
        }),
        required=True
    )
    
    hire_date = forms.DateField(
        widget=forms.DateInput(attrs={
            'type': 'date',
            'class': 'w-full p-2 mb-4 border rounded'
        }),
        required=True
    )
    
    contact_number = forms.CharField(
        max_length=20,
        widget=forms.TextInput(attrs={
            'placeholder': 'Contact Number',
            'class': 'w-full p-2 mb-4 border rounded'
        })
    )
    
    salary = forms.DecimalField(
        max_digits=10,
        decimal_places=2,
        widget=forms.NumberInput(attrs={
            'placeholder': 'Salary',
            'class': 'w-full p-2 mb-4 border rounded'
        }),
        help_text="Enter the monthly salary of the employee in dollars."
    )
    
    position = forms.ModelChoiceField(
        queryset=Group.objects.all(),
        widget=forms.Select(attrs={
            'class': 'w-full p-2 mb-4 border rounded'
        })
    )

    username = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={
            'placeholder': 'Username',
            'class': 'w-full p-2 mb-4 border rounded'
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Password',
            'class': 'w-full p-2 mb-4 border rounded'
        })
    )
    
    class Meta:
        model = Employee
        fields = (
            "first_name",
            "last_name",
            "gender",
            "birth_date",
            "hire_date",
            "contact_number",
            "salary",
        )
        
    def save(self, commit=True):
        # Create the User account first
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        
        # Create the User instance
        user = User.objects.create_user(username=username, password=password)

        # Create the Employee instance, associating it with the created User
        employee = super().save(commit=False)
        employee.account = user

        if commit:
            employee.save()
            # Save positions to the related User instance
            position = self.cleaned_data['position']
            user.groups.add(position)
        return employee
    
    user = User.objects.get(id=1)
    user.groups.name
    
    def clean_hire_date(self):
        hire_date = self.cleaned_data.get('hire_date')
        if hire_date and hire_date > date.today():
            raise forms.ValidationError("Please enter a valid hire date that is not in the future.")
        return hire_date
    
    def clean_contact_number(self):
        contact_number = self.cleaned_data.get('contact_number')
        if not contact_number.isdigit():
            raise forms.ValidationError("Contact number should contain only digits.")
        if len(contact_number) < 10:
            raise forms.ValidationError("Contact number must be at least 10 digits.")
        return contact_number
    
    def clean_salary(self):
        salary = self.cleaned_data.get('salary')
        if salary and salary <= 0:
            raise forms.ValidationError("Salary must be greater than zero.")
        return salary
    
    def clean(self):
        cleaned_data = super().clean()
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')

        # Check if another employee with the same first name and last name exists
        if Employee.objects.filter(first_name=first_name, last_name=last_name).exists():
            raise forms.ValidationError(f"An employee with the name '{first_name} {last_name}' already exists.")
        
        return cleaned_data

