from .models import Order
from customers.models import Customer
from products.models import Medicine
from django.views.generic import ListView,CreateView

class add_order(CreateView):
    model = Order
    fields = '__all__'

class order_list(ListView):
    model = Order

