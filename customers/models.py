from django.db import models
from django.contrib.auth.models import AbstractUser
from orders.common import Create_Update_Time

class Customer(Create_Update_Time):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    phone = models.CharField(max_length=11)
    address=models.CharField(max_length=50)
    city=models.CharField(max_length=20)

    def __str__(self):
        return self.name