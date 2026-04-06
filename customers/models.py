from django.db import models
from orders.common import CreateUpdateTime
from django.contrib.auth.models import AbstractUser

class Customer(AbstractUser,CreateUpdateTime):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    phone = models.CharField(max_length=11, null=True, blank=True)
    address=models.CharField(max_length=50, null=True, blank=True)
    city=models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.username