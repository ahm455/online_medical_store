from django.contrib import admin
from .models import Order, OrderedItem, Profit

admin.site.register(Profit)
admin.site.register(Order)