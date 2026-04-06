from rest_framework import serializers
from .models import Customer

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['username', 'password','name', 'email','age', 'phone','is_superuser','is_staff', 'address','city']