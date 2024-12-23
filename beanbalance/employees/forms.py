from django import forms
from .models import Employee
from django.contrib.auth.models import User, Group
from django.contrib.auth.password_validation import validate_password
from datetime import date
from django.core.exceptions import ValidationError

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
        
    def clean_first_name(self):
        first_name = self.cleaned_data.get("first_name")
        
        if first_name and not first_name.isalpha():
            raise forms.ValidationError("First name should not contain numbers.")
        return first_name   
    
    def clean_last_name(self):
        last_name = self.cleaned_data.get("last_name")     
        if last_name and not last_name.isalpha():
            raise forms.ValidationError("Last name should not contain numbers.")
        return last_name
 
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError(f"The username '{username}' is already taken. Please choose a different username.")
        return username

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
    
    def clean_birth_date(self):
        birth_date = self.cleaned_data.get('birth_date')
        if birth_date and birth_date.year > 2004 :
            raise forms.ValidationError("Please enter a valid birth date correctly.")
        return birth_date
    
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
    
    def clean_password(self):
        password = self.cleaned_data.get('password')
        
        # Use Django's built-in password validator
        try:
            validate_password(password)
        except ValidationError as e:
            raise forms.ValidationError(e.messages)
        return password
