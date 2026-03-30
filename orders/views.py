from django.shortcuts import render, redirect
from django.utils import timezone
from datetime import timedelta
from django.db.models import Sum
from .models import Order, Profit
from customers.models import Customer
from products.models import Medicine, Stock
from .serializers import OrderedItemSerializer, OrderSerializer

def add_order(request):
    customers = Customer.objects.all()
    medicines = Medicine.objects.all()

    if request.method == 'POST':
        order_serializer = OrderSerializer(data=request.POST)
        if order_serializer.is_valid():
            order = order_serializer.save()
            
            medicine_id = int(request.POST['medicine'])
            medicine = Medicine.objects.get(id=medicine_id)
            quantity = int(request.POST['quantity'])

            ordered_item_serializer = OrderedItemSerializer(data={
                'order': order.id,
                'medicine': medicine.id,
                'quantity': quantity
            })
            if ordered_item_serializer.is_valid():
                item = ordered_item_serializer.save()
                ordered_item_serializer.calculate_profit(order)
                return redirect('orders:order_list')

    else:
        order_serializer = OrderSerializer()
        ordered_item_serializer = OrderedItemSerializer()

    return render(request, 'orders/add_order.html', {
        'order_serializer': order_serializer,
        'ordered_item_serializer': ordered_item_serializer,
        'customers': customers,
        'medicines': medicines
    })

def order_list(request):
    orders = Order.objects.all()
    for order in orders:
        if order.total_amount is None:
            order.total_amount = 0
            
    return render(request, 'orders/order_list.html', {'orders': orders})

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
    return render(request, 'orders/dashboard.html', context)

def profit_report(request):
    profits = Profit.objects.select_related('order', 'order__customer').all()
    today = timezone.now()
    start_week = today - timedelta(days=today.weekday())
    start_week = start_week.replace(hour=0, minute=0, second=0, microsecond=0)
    weekly_profits = Profit.objects.filter(order__created_at__gte=start_week).aggregate(total=Sum('profit_amount'))['total'] or None
    start_month = today.replace(day=1)
    monthly_profits = Profit.objects.filter(order__created_at__gte=start_month).aggregate(total=Sum('profit_amount'))['total'] or 0
    context = {
        'profits': profits,
        'weekly_profits': weekly_profits,
        'monthly_profits': monthly_profits,
    }
    return render(request, 'orders/profit.html', context)

def order_shipped(request, order_id):
    order = Order.objects.get(id=order_id)
    order.status = 'Shipped'
    order.save()
    return redirect('orders:order_list')    

def order_delivered(request, order_id):
    order = Order.objects.get(id=order_id)
    order.status = 'Delivered'
    order.save()
    return redirect('orders:order_list')