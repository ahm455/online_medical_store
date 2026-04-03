from django.contrib import admin
from .models import Order,OrderedItems

admin.site.register(Order)
admin.site.register(OrderedItems)
