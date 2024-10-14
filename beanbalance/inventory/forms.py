from django import forms
from .models import Category

class CategoryForm(forms.ModelForm):
    name = forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={
            'placeholder': 'Category Name',
            'class': 'w-full p-2 mb-4 border rounded'
        })
    )

    price = forms.DecimalField(
        max_digits=10,
        decimal_places=2,
        widget=forms.NumberInput(attrs={
            'placeholder': 'Price',
            'class': 'w-full p-2 mb-4 border rounded'
        })
    )

    quantity = forms.IntegerField(
        widget=forms.NumberInput(attrs={
            'placeholder': 'Quantity',
            'class': 'w-full p-2 mb-4 border rounded'
        })
    )

    class Meta:
        model = Category
        fields = ('name', 'price', 'quantity')
    
    def clean_name(self):
        name = self.cleaned_data.get('name')
        if Category.objects.filter(name__iexact=name).exists():
            raise forms.ValidationError(f"The '{name}' already exists.") 
        return name