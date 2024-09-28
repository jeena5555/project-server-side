from django import forms
from django.forms import ModelForm, DateInput
from order.models import Order
from datetime import date



class DateFilterForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['order_date']
        widgets = {
            'order_date': DateInput(
                attrs={
                    'type': 'date',
                    'class': 'border-2 text-black rounded-lg py-2 px-4',
                    })
        }
