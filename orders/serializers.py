from rest_framework import serializers
from .models import Order,OrderedItems
from products.models import Medicine
from django.db.models import Sum
from django.db.models.functions import TruncDate

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'customer','payment_method','payment_status']


class OrderedItemSerializer(serializers.ModelSerializer):
    medicine_name = serializers.CharField(source='medicine.name', read_only=True)
    customer_name = serializers.CharField(source='order.customer.name', read_only=True)
    class Meta:
        model = OrderedItems
        fields = '__all__'

    def create(self, validated_data):
        medicine = validated_data['medicine']
        quantity = validated_data['quantity']
        order = validated_data['order']


        item = OrderedItems.objects.create(**validated_data)

        medicine.quantity -= quantity
        medicine.save()

        items = order.items.all()

        total = 0
        profit = 0

        for i in items:
            total += i.medicine.selling_price * i.quantity
            profit += (i.medicine.selling_price - i.medicine.cost_price) * i.quantity

        order.total_amount = total
        order.profit_amount = profit
        order.save()

        return item




