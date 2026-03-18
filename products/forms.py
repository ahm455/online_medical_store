from rest_framework import serializers
from .models import Medicine, OrderedItem, Customer, Order, Stock

class medicineForm(serializers.ModelSerializer):
    class Meta:
        model = Medicine
        fields = ['id', 'medicine_name', 'potency', 'cost_price', 'selling_price']

class customerform(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'name', 'age', 'phone']

class OrderedItemsForm(serializers.ModelSerializer):
    customer = serializers.PrimaryKeyRelatedField(queryset=Customer.objects.all())
    medicine = serializers.PrimaryKeyRelatedField(queryset=Medicine.objects.all())

    class Meta:
        model = OrderedItem
        fields = ['id', 'customer', 'medicine', 'quantity']

class OrderForm(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'status', 'payment_status', 'payment_method']

class StockForm(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = ['id', 'medicine', 'quantity']

    def create(self, validated_data):
        medicine = validated_data['medicine']
        quantity = validated_data['quantity']
        stock_instance, created = Stock.objects.get_or_create(medicine=medicine)
        if not created:
            stock_instance.quantity += quantity
            stock_instance.save()
        else:
            stock_instance.quantity = quantity
            stock_instance.save()
        return stock_instance