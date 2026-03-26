from rest_framework import serializers
from .models import Medicine, Stock

class MedicineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicine
        fields = '__all__'


class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = '__all__'

    def create(self, validated_data):
        medicine = validated_data['medicine']
        quantity = validated_data['quantity']

        stock, created = Stock.objects.get_or_create(medicine=medicine)

        if not created:
            stock.quantity += quantity
        else:
            stock.quantity = quantity

        stock.save()
        return stock