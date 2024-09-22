from django.db import models

# Create your models here.

class Account(models.Model):
    account_name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)


class Employee(models.Model):

    class Gender(models.TextChoices):
        M = "M", "Male"
        F = "F", "Female"
        LGBT = "LGBT", "LGBT"

    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=200)
    gender = models.CharField(max_length=10, choices=Gender.choices)
    birth_date = models.DateField()
    hire_date = models.DateField()
    contact_number = models.CharField(max_length=20)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    position = models.ForeignKey("Position", on_delete=models.CASCADE)
    account = models.OneToOneField("Account", on_delete=models.CASCADE)


class Position(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(blank=True, null=True)


