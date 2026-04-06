from django.db import models
from django.contrib.auth.models import User
from orders.common import CreateUpdateTime
from django.contrib.auth.models import AbstractUser

class Customer(CreateUpdateTime,AbstractUser):
    # user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='customer')
    name = models.CharField(max_length=20, null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    phone = models.CharField(max_length=11, null=True, blank=True)
    address=models.CharField(max_length=50, null=True, blank=True)
    city=models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.name