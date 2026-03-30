from django.shortcuts import render, redirect,get_object_or_404
from .models import Medicine, Stock
from .serializer import MedicineSerializer, StockSerializer

def add_medicine(request):
    if request.method == 'POST':
        serializer = MedicineSerializer(data=request.POST)
        if serializer.is_valid():
            serializer.save()
            return redirect('products:medicine_list')
    else:
        serializer = MedicineSerializer()

    return render(request, 'products/add_medicine.html', {'serializer': serializer})

def medicine_list(request):
    medicines = Medicine.objects.all()
    return render(request, 'products/medicine_list.html', {'medicines': medicines})

def add_stock(request):

    if request.method == 'POST':
        serializer = StockSerializer(data=request.POST)
        if serializer.is_valid():
            serializer.save()
            return redirect('products:stock_list')
    else:
        serializer = StockSerializer()

    return render(request, 'products/add_stock.html', {
        'serializer': serializer,
    })



def stock_list(request):
    stocks = Stock.objects.all()
    return render(request, 'products/stock_list.html', {'stocks': stocks})

def edit_medicine(request,id):
    medicine=get_object_or_404(Medicine,id=id)

    if request.method=='POST':
        serializer=MedicineSerializer(medicine,data=request.POST)
        if serializer.is_valid():
            serializer.save()
            return redirect('products:medicine_list')
    else:
        serializer=MedicineSerializer(medicine)
    return render  (request,'products/edit_medicine.html',{'serializer':serializer,'medicine': medicine})