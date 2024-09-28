from django import template

register = template.Library()

@register.filter(name='multiply')
def multiply(value, arg):
    try:
        return value * arg
    except (ValueError, TypeError):
        return ''

@register.filter(name='total_quantity')
def total_quantity(order_menus):
    """Calculates the total quantity of all order menus."""
    return sum(item.quantity for item in order_menus)

@register.filter(name='add_class')
def add_class(field, css):
    # Check if the input is a field before calling as_widget
    if hasattr(field, 'as_widget'):
        return field.as_widget(attrs={"class": css})
    return field
