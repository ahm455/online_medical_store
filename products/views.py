from django.shortcuts import render,redirect
from .models import Medicine, ordereditems,order,Customer
from .forms import medicineForm,OrderedItemsForm,customerForm


def medicine_list(request):
    medicines = Medicine.objects.all()
    return render(request, 'medicine_list.html', {'medicines': medicines})

def order_list(request):
    orders = ordereditems.objects.all()
    return render(request, 'order_list.html', {'orders': orders})

def add_medicine(request):
    if request.method == 'POST':
            form = medicineForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('medicine_list')
    else:
        form=medicineForm()        
    return render(request,'add_medicine.html',{'form':form})


def add_order(request):
    if request.method == 'POST':
        form = OrderedItemsForm(request.POST)
        if form.is_valid():
            new_order = order.objects.create(customer=form.cleaned_data['customer'])
            ordered_item = form.save(commit=False)
            ordered_item.order = new_order 
            ordered_item.save()
            return redirect('order_list')
    else:
            form=OrderedItemsForm()         
    return render(request,'add_order.html',{'form':form})        

def dashboard(request):
    return render(request,'dashboard.html')    


def add_customer(request):
    if request.method == 'POST':
        form = customerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customer_list') 
    else:
        form = customerForm()
    return render(request, 'add_customer.html', {'form': form})


def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'customer_list.html', {'customers': customers})