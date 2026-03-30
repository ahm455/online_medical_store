from django.shortcuts import render, redirect
from .models import Customer
from .serializers import CustomerSerializer

def add_customer(request):
    if request.method == 'POST':
        serializer = CustomerSerializer(data=request.POST)
        if serializer.is_valid():
            serializer.save()
            return redirect('customers:customer_list')
    else:
        serializer = CustomerSerializer()

    return render(request, 'customers/add_customer.html', {'serializer': serializer})


def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'customers/customer_list.html', {'customers': customers})