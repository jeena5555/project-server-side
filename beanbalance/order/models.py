from django.db import models
from menu.models import Menu
from django.contrib.auth.models import User # Employee

# Create your models here.

class Order(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    order_date = models.DateField()
    order_time = models.TimeField()
    employee = models.ForeignKey(User, on_delete=models.CASCADE)
    menus = models.ManyToManyField(Menu, through="OrderMenu")

class Payment(models.Model):
    class PaymentMethod(models.TextChoices):
        Cash = "Cash"
        Credit = "Credit"
        QR = "QR Code"
    order = models.OneToOneField("order.Order", on_delete=models.PROTECT)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=20, choices=PaymentMethod.choices)
    payment_date = models.DateField()
    payment_time = models.TimeField()

class OrderMenu(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    class Meta:
        unique_together = ("order", "menu")

    def __str__(self):
        return f"Order {self.order.id} - Menu {self.menu.name} - Quantity {self.quantity}"
