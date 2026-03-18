from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from datetime import timedelta
from django.db.models import Sum
from .models import Customer, Medicine, Stock, Order, OrderedItem, Profit
from .forms import customerform, medicineForm, StockForm, OrderedItemsForm, OrderForm

def dashboard(request):
    total_orders = Order.objects.count()
    pending_orders = Order.objects.filter(status='Pending').count()
    shipped_orders = Order.objects.filter(status='Shipped').count()
    delivered_orders = Order.objects.filter(status='Delivered').count()
    total_customers = Customer.objects.count()
    total_medicines = Medicine.objects.count()
    stocks = Stock.objects.all()
    weekly_profits = Profit.objects.filter(
        order__created_at__gte=timezone.now() - timedelta(days=7)
    ).aggregate(total_profit=Sum('profit_amount'))['total_profit'] or 0
    monthly_profits = Profit.objects.filter(
        order__created_at__gte=timezone.now() - timedelta(days=30)
    ).aggregate(total_profit=Sum('profit_amount'))['total_profit'] or 0
    total_medicine_value = sum(stock.quantity * stock.medicine.selling_price for stock in stocks)
    context = {
        'weekly_profits': weekly_profits,
        'monthly_profits': monthly_profits,
        'total_orders': total_orders,
        'pending_orders': pending_orders,
        'shipped_orders': shipped_orders,
        'delivered_orders': delivered_orders,
        'total_customers': total_customers,
        'total_medicines': total_medicines,
        'total_medicine_value': total_medicine_value,
    }
    return render(request, 'dashboard.html', context)

def add_customer(request):
    if request.method == 'POST':
        serializer = customerform(data=request.POST)
        if serializer.is_valid():
            serializer.save()
            return redirect('customer_list')
    else:
        serializer = customerform()
    return render(request, 'add_customer.html', {'form': serializer})

def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'customer_list.html', {'customers': customers})

def add_medicine(request):
    if request.method == 'POST':
        serializer = medicineForm(data=request.POST)
        if serializer.is_valid():
            serializer.save()
            return redirect('medicine_list')
    else:
        serializer = medicineForm()
    return render(request, 'add_medicine.html', {'serializer': serializer})

def medicine_list(request):
    medicines = Medicine.objects.all()
    return render(request, 'medicine_list.html', {'medicines': medicines})

def add_stock(request):
    if request.method == 'POST':
        serializer = StockForm(data=request.POST)
        if serializer.is_valid():
            serializer.save()
            return redirect('stock_list')
    else:
        serializer = StockForm()
    return render(request, 'add_stock.html', {'form': serializer})

def stock_list(request):
    stocks = Stock.objects.all()
    return render(request, 'stock_list.html', {'stocks': stocks})

def update_stock(request, stock_id):
    stock_instance = get_object_or_404(Stock, id=stock_id)
    if request.method == 'POST':
        serializer = StockForm(stock_instance, data=request.POST)
        if serializer.is_valid():
            serializer.save()
            return redirect('stock_list')
    else:
        serializer = StockForm(stock_instance)
    return render(request, 'update_stock.html', {'form': serializer})

def add_order(request):
    if request.method == 'POST':
        order_serializer = OrderForm(data=request.POST)
        items_serializer = OrderedItemsForm(data=request.POST)
        if order_serializer.is_valid() and items_serializer.is_valid():
            order = order_serializer.save()
            item = items_serializer.save(order=order, customer=order.customer)
            profit_record = Profit.objects.create(order=order)
            profit_record.calculate_profit()
            return redirect('order_list')
    else:
        order_serializer = OrderForm()
        items_serializer = OrderedItemsForm()
    return render(request, 'add_order.html', {'order_form': order_serializer, 'items_form': items_serializer})

def order_list(request):
    orders = Order.objects.all()
    if request.method == 'POST':
        for order in orders:
            serializer = OrderForm(order, data=request.POST, partial=True, prefix=f'order_{order.id}')
            if serializer.is_valid():
                serializer.save()
        return redirect('order_list')
    order_forms = [{'order': order, 'form': OrderForm(order, prefix=f'order_{order.id}')} for order in orders]
    return render(request, 'order_list.html', {'order_forms': order_forms})

def profit_report(request):
    profits = Profit.objects.all()
    weekly_profits = Profit.objects.filter(
        order__created_at__gte=timezone.now() - timedelta(days=7)
    ).aggregate(total_profit=Sum('profit_amount'))['total_profit'] or 0
    monthly_profits = Profit.objects.filter(
        order__created_at__gte=timezone.now() - timedelta(days=30)
    ).aggregate(total_profit=Sum('profit_amount'))['total_profit'] or 0
    return render(request, 'profit.html', {'profits': profits, 'weekly_profits': weekly_profits, 'monthly_profits': monthly_profits})