from rest_framework import serializers
from .models import Medicine, Stock

class MedicineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicine
        fields = ['medicine_name','potency','cost_price','selling_price','expiry_date']


class StockSerializer(serializers.ModelSerializer):
    medicine = serializers.PrimaryKeyRelatedField(
        queryset=Medicine.objects.all()  # <-- This ensures all medicines appear
    )
    class Meta:
        model = Stock
        fields = '__all__'

    def create(self, validated_data):
        medicine = validated_data['medicine']
        quantity_to_add = validated_data.get('quantity', 0)

        stock, created = Stock.objects.get_or_create(
            medicine=medicine,
            defaults={'quantity': 0} 
        )

        stock.quantity += quantity_to_add
        stock.save()

        return stock