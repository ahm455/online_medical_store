from django.shortcuts import render,redirect
from .models import Medicine, ordereditems,order,Customer
from .forms import medicineForm,OrderedItemsForm,customerForm
from rest_framework.parsers import JSONParser

def dashboard(request):
    return render(request,'dashboard.html')  
def add_medicine(request):
    if request.method == 'POST':
            data = request.POST.dict()
            serializer = medicineForm(data=data)
            if serializer.is_valid():
                serializer.save()
                return redirect('medicine_list')
    else:
        serializer=medicineForm()        
    return render(request,'add_medicine.html',{'serializer':serializer})
def medicine_list(request):
    medicines = Medicine.objects.all()
    return render(request, 'medicine_list.html', {'medicines': medicines})


def add_order(request):
    if request.method == 'POST':
        data = request.POST.dict()
        serializer = OrderedItemsForm(data=data)
        if serializer.is_valid():
            new_order = order.objects.create(customer=serializer.validated_data['customer'])
            ordered_item = serializer.save(commit=False)
            ordered_item.order = new_order 
            ordered_item.save()
            return redirect('order_list')
    else:
            serializer=OrderedItemsForm()         
    return render(request,'add_order.html',{'serializer':serializer})          
def order_list(request):
    orders = ordereditems.objects.all()
    return render(request, 'order_list.html', {'orders': orders})


def add_customer(request):
    if request.method == 'POST':    
        serializer = customerForm(data=request.POST)
        if serializer.is_valid():
            serializer.save()
            return redirect('customer_list') 
    else:
        serializer = customerForm()
    return render(request, 'add_customer.html', {'serializer': serializer})


def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'customer_list.html', {'customers': customers})
