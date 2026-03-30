from rest_framework import serializers
from .models import Medicine, Stock

class MedicineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicine
        fields = ['medicine_name','potency','cost_price','selling_price',]


class StockSerializer(serializers.ModelSerializer):
    medicine = serializers.PrimaryKeyRelatedField(
        queryset=Medicine.objects.all()  # <-- This ensures all medicines appear
    )
    class Meta:
        model = Stock
        fields = '__all__'