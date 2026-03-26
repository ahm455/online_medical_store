from rest_framework import serializers
from .models import Order, OrderedItem, Profit
from products.models import Stock


class OrderedItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderedItem
        fields = '__all__'

    def create(self, validated_data):
        medicine = validated_data['medicine']
        quantity = validated_data['quantity']
        order = validated_data['order']

        selling_price = medicine.selling_price
        total_price = selling_price * quantity
        profit = (selling_price - medicine.cost_price) * quantity

        item = OrderedItem.objects.create(
            **validated_data,
            selling_price=selling_price,
            total_price=total_price,
            profit_per_item=profit
        )

        stock = Stock.objects.get(medicine=medicine)
        stock.quantity -= quantity
        stock.save()

        order.update_total()
        return item


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'