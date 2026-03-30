from rest_framework import serializers
from .models import Order, OrderedItem, Profit
from products.models import Stock
from django.db.models import Sum


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
    def calculate_profit(self, order):
        total_profit = order.ordereditem_set.aggregate(
            total=Sum('profit_per_item')
        )['total'] or 0

        Profit.objects.update_or_create(
            order=order,
            defaults={'profit_amount': total_profit}
        )
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'




