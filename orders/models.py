from django.db import models
from customers.models import Customer
from products.models import Medicine
from orders.common import *

class Order(CreateUpdateTime):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE,related_name="customers")
    medicine = models.ManyToManyField(Medicine, through='OrderedItems')

    status = models.CharField(max_length=10, choices=choices.status, default=choices.status[0])
    payment_status = models.CharField(max_length=10, choices=choices.payment_status, default=choices.payment_status[0])
    payment_method = models.CharField(max_length=10, choices=choices.payment_method, blank=True)

    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    profit_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.customer} ({self.total_amount})"


class OrderedItems(CreateUpdateTime):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE,related_name="medicines")
    quantity = models.IntegerField()

    def __str__(self):
        return f"{self.order} ({self.medicine})"
