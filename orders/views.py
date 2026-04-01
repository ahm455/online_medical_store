from django.views.generic import ListView,CreateView
from .models import Order
from django.urls import reverse_lazy
from customers.models import Customer
from products.models import Medicine
from django.db.models.functions import TruncDate
from django.db.models import Sum


class add_order(CreateView):
    model = Order
    fields = ['customer','medicine','quantity','status','payment_status','payment_method']
    success_url = reverse_lazy('orders:order_list') 

    def form_valid(self, form):
        order = form.save(commit=False)
        medicine = order.medicine
        quantity = order.quantity
        cost_price = medicine.cost_price
        selling_price = medicine.selling_price
        order.selling_price = selling_price
        order.total_amount = selling_price * quantity
        order.profit_amount = (selling_price - cost_price) * quantity
        order.save()
        return super().form_valid(form)

class order_list(ListView):
    model = Order
    template_name = "order_list.html" 

class daily_profit(ListView):
    template_name = "orders/daily_profit.html"
    context_object_name = "profits"

    def get_queryset(self):
        qs = (
            Order.objects
            .values(date=TruncDate('created_at'))
            .annotate(total_profit=Sum('profit_amount'))
            .order_by('-date')
        )
        return qs