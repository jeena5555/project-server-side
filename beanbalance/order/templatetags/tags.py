from django import template

register = template.Library()


@register.filter(name="multiply")
def multiply(value, arg):
    try:
        return value * arg
    except (ValueError, TypeError):
        return ""


@register.filter(name="total_quantity")
def total_quantity(order_menus):
    """Calculates the total quantity of all order menus."""
    return sum(item.quantity for item in order_menus)


@register.filter(name="add_class")
def add_class(field, css):
    # Check if the input is a field before calling as_widget
    if hasattr(field, "as_widget"):
        return field.as_widget(attrs={"class": css})
    return field


@register.simple_tag(takes_context=True)
def get_navbar(context):
    user = context["request"].user
    if user.is_authenticated:
        if user.groups.filter(name="Manager").exists():
            return "navbar_manager.html"
        elif user.groups.filter(name="Cashier").exists():
            return "navbar_cashier.html"

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)
