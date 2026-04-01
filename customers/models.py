from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='customer')
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    phone = models.CharField(max_length=11)
    address=models.CharField(max_length=50)
    city=models.CharField(max_length=20)

    def __str__(self):
        return self.name