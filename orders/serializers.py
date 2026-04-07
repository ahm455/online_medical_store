from rest_framework import serializers
from .models import Order,OrderedItems
from django.core.exceptions import ValidationError
from django.utils import timezone
from datetime import timedelta,date
from products.models import Medicine


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


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
        today = date.today()

        item = OrderedItems.objects.create(**validated_data)

        medicine.quantity -= quantity
        if medicine.quantity < 0:
            raise ValidationError("No stock avaliable")
        if medicine.expiry_date < timezone.now().date() or medicine.expiry_date<= today + timedelta(days=20):
            raise ValidationError("The expiry date is very near or past.")

        medicine.save()

        medicines = validated_data['medicine']
        total = order.total_amount
        profit = order.profit_amount
        total += medicines.selling_price * medicines.quantity
        profit += (medicines.selling_price - medicines.cost_price) * medicines.quantity

        order.total_amount = total
        order.profit_amount = profit
        order.save()

        return item

    def update(self, instance, validated_data):
        old_quantity = instance.quantity
        old_medicine = instance.medicine
        new_medicine = validated_data.get('medicine', old_medicine)
        new_quantity = validated_data.get('quantity', old_quantity)
        order = validated_data.get('order', instance.order)

        today = date.today()

        if old_medicine != new_medicine:
            old_medicine.quantity += old_quantity
            old_medicine.save()
            stock_change = new_quantity
        else:
            stock_change = new_quantity - old_quantity

        if new_medicine.quantity - stock_change < 0:
            raise ValidationError("No stock available for the selected medicine.")

        if new_medicine.expiry_date < timezone.now().date() or new_medicine.expiry_date <= today + timedelta(days=20):
            raise ValidationError("The expiry date is very near or past.")

        instance.medicine = new_medicine
        instance.quantity = new_quantity
        instance.save()

        new_medicine.quantity -= stock_change
        new_medicine.save()

        total = 0
        profit = 0
        for product in order.items.all():
            total += product.medicine.selling_price * product.quantity
            profit += (product.medicine.selling_price - product.medicine.cost_price) * product.quantity

        order.total_amount = total
        order.profit_amount = profit
        order.save()

        return instance




