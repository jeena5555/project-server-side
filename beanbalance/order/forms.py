from django import forms
from django.forms import ModelForm, DateInput
from order.models import Order
from datetime import date
from django.utils import timezone

class DateFilterForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['order_date']
        widgets = {
            'order_date': forms.DateInput(
                attrs={
                    'type': 'date',
                    'value': timezone.now().date(),
                }
            ),
        }

