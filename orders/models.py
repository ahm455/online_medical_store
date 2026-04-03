from django.db import models
from customers.models import Customer
from products.models import Medicine
from orders.common import *


class Order(Payment_Choices, Status_choices, Payment_methods, Create_Update_Time):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    medicine = models.ManyToManyField(Medicine, through='OrderedItems')

    status = models.CharField(max_length=10, choices=Status_choices.STATUS_CHOICES, default='Pending')
    payment_status = models.CharField(max_length=10, choices=Payment_Choices.PAYMENT_STATUS, default='Unpaid')
    payment_method = models.CharField(max_length=10, choices=Payment_methods.PAYMENT_METHOD, blank=True)

    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    profit_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)


class OrderedItems(Create_Update_Time):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    quantity = models.IntegerField()
