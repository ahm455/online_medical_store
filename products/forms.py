from django import forms
from .models import Medicine, ordereditems,Customer,order
from django.contrib.auth.models import User
from rest_framework import serializers


class medicineForm(serializers.ModelSerializer):
    class Meta:
        model = Medicine
        fields = ['medicine_name', 'potency', 'cost_price', 'selling_price']


class OrderedItemsForm(serializers.ModelSerializer):
    class Meta:
        model = ordereditems
        fields = ['customer', 'medicine', 'quantity']

OrderedItemsFormSet = forms.inlineformset_factory(
    order, ordereditems, form=OrderedItemsForm,
    extra=1, can_delete=True
)

class OrderForm(serializers.ModelSerializer):
    class Meta:
        model = order
        fields = ['customer']       




class customerForm(serializers.ModelSerializer):
    username = serializers.CharField(max_length=150)
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Customer
        fields = ['name', 'age', 'phone', 'username', 'email', 'password']

    def create(self, validated_data):
        username = validated_data.pop('username')
        email = validated_data.pop('email')
        password = validated_data.pop('password')

        user = User.objects.create_user(username=username, email=email, password=password)

        customer = Customer.objects.create(user=user, **validated_data)
        return customer