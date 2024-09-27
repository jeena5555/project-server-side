from django import forms
from .models import Employee,User
from datetime import date
class AddEmployeeForm(forms.ModelForm):
    first_name = forms.CharField(max_length=150)
    last_name = forms.CharField(max_length=200)
    gender = forms.ChoiceField(choices=Employee.Gender.choices) # Using choices directly from the Gender class defined in the model
    birth_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), required=True)
    hire_date = forms.DateField(widget=forms.SelectDateWidget) #no idea
    contact_number = forms.CharField(max_length=20)
    salary = forms.DecimalField(max_digits=10, decimal_places=2)
    account = forms.ModelChoiceField(queryset=User.objects.all(), empty_label="Select User")
    class Meta:
        model = Employee
        fields = ("first_name",
                  "last_name",
                  "gender",
                  "birth_date",
                  "hire_date",
                  "contact_number",
                  "salary",
                  "account"
                  )
    def clean_hire_date(self):
      cleaned_data = super().clean()
      hire_date = cleaned_data.get('hire_date')
      if hire_date > date.today():
          msg = "Please Enter hire date correctly"
          self.add_error("hire_date", msg)
      return hire_date