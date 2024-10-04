from django.db import models
from django.contrib.auth.models import User

# class Account = auth_user
# field : username , password

# class Position = auth_group
# field : name

## auth_user many to many with auth_group


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
    account = models.OneToOneField(User, on_delete=models.CASCADE)