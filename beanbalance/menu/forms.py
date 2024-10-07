from django import forms
from .models import Menu, Category

# Form for adding/editing a Category
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'w-full p-2 mb-4 border rounded',
                'placeholder': 'Category Name',
            }),
        }

# Form for adding/editing a Menu item
class MenuForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = ['name', 'description', 'price', 'category']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'w-full p-2 mb-4 border rounded',
                'placeholder': 'Menu Name',
            }),
            'description': forms.Textarea(attrs={
                'class': 'w-full p-2 mb-4 border rounded',
                'placeholder': 'Description',
            }),
            'price': forms.NumberInput(attrs={
                'class': 'w-full p-2 mb-4 border rounded',
                'placeholder': 'Price',
            }),
            'category': forms.Select(attrs={
                'class': 'w-full p-2 mb-4 border rounded',
            }),
        }
