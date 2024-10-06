from django import forms
from django.utils import timezone

class SelectSalesTrendsForm(forms.Form):
    DATE_CHOICES = [
        ('week', 'Week'),
        ('month', 'Month'),
        ('year', 'Year'),
    ]

    select = forms.ChoiceField(
        choices=DATE_CHOICES,
        label="Select Trend",
        widget=forms.Select(attrs={
            'class': 'w-20 p-2 border rounded'
        }),
    )

class GenerateReportForm(forms.Form):
    date = forms.DateField(
        widget=forms.DateInput(attrs={
            'type': 'date',
            'class': 'w-full p-2 mb-4 border rounded',
            'value': timezone.now().date(),
        }),
    )
