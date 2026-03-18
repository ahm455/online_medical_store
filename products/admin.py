from django.contrib import admin
from .models import Customer, Medicine, Order, OrderedItem,Profit

admin.site.register(Order)
admin.site.register(OrderedItem)
admin.site.register(Customer)
admin.site.register(Profit)