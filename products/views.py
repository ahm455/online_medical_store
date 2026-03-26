from django.shortcuts import render, redirect
from .models import Medicine, Stock
from .serializer import MedicineSerializer, StockSerializer


def add_medicine(request):
    if request.method == "POST":
        serializer = MedicineSerializer(data=request.POST)
        if serializer.is_valid():
            serializer.save()
            return redirect('products:medicine_list')

    return render(request, 'products/add_medicine.html', {'serializer': serializer})


def medicine_list(request):
    medicines = Medicine.objects.all()
    return render(request, 'products/medicine_list.html', {'medicines': medicines})


def add_stock(request):
    if request.method == 'POST':
        serializer = StockSerializer(data=request.POST)
        if serializer.is_valid():
            serializer.save()
            return redirect('stock_list')
    else:
        serializer = StockSerializer()

    return render(request, 'products/add_stock.html', {'form': serializer})


def stock_list(request):
    stocks = Stock.objects.all()
    return render(request, 'products/stock_list.html', {'stocks': stocks})