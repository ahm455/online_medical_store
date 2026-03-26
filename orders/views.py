from django.shortcuts import render, redirect
from .models import Order, Profit,Customer
from products.models import Stock,Medicine
from .serializers import OrderSerializer, OrderedItemSerializer
from django.utils import timezone
from datetime import timedelta
from django.db.models import Sum


def add_order(request):
    if request.method == 'POST':
        order_serializer = OrderSerializer(data=request.POST)
        item_serializer = OrderedItemSerializer(data=request.POST)

        if order_serializer.is_valid() and item_serializer.is_valid():
            order = order_serializer.save()
            item_serializer.save(order=order)

            profit = Profit.objects.create(order=order)
            profit.calculate_profit()

            return redirect('order_list')

    else:
        order_serializer = OrderSerializer()
        item_serializer = OrderedItemSerializer()

    return render(request, 'orders/add_order.html', {
        'order_form': order_serializer,
        'item_form': item_serializer
    })


def order_list(request):
    orders = Order.objects.all()
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
    start_week = today - timezone.timedelta(days=today.weekday())
    weekly_profits = Profit.objects.filter(order__created_at__gte=start_week).aggregate(total=Sum('profit_amount'))['total'] or 0
    start_month = today.replace(day=1)
    monthly_profits = Profit.objects.filter(order__created_at__gte=start_month).aggregate(total=Sum('profit_amount'))['total'] or 0
    context = {
        'profits': profits,
        'weekly_profits': weekly_profits,
        'monthly_profits': monthly_profits,
    }
    return render(request, 'orders/profit.html', context)