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

class OrderedItemsSerializer(serializers.ModelSerializer):
    customer = serializers.PrimaryKeyRelatedField(queryset=Customer.objects.all())
    medicine = serializers.PrimaryKeyRelatedField(queryset=Medicine.objects.all())

    class Meta:
        model = OrderedItem
        fields = ['id', 'order', 'customer', 'medicine', 'quantity']

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