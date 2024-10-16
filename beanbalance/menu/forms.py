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
    def clean_name(self):
        name = self.cleaned_data.get('name')
        if Category.objects.filter(name__iexact=name).exists():
            raise forms.ValidationError(f"The category '{name}' already exists.") 
        return name

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
    def clean_name(self):
        name = self.cleaned_data.get('name')
        if Menu.objects.filter(name__iexact=name).exists():
            raise forms.ValidationError(f"The '{name}' already exists.") 
        return name
    
    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price and price < 0 :
            raise forms.ValidationError(f"Please enter value more than zero") 
        return price
