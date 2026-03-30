from django.db import models
from django.db.models import Sum
from customers.models import Customer
from products.models import Medicine


class Order(models.Model):

    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Shipped', 'Shipped'),
        ('Delivered', 'Delivered'),
    ]

    PAYMENT_STATUS = [
        ('Paid', 'Paid'),
        ('Unpaid', 'Unpaid'),
    ]

    PAYMENT_METHOD = [
        ('Cash', 'Cash'),
        ('Card', 'Card'),
        ('Online', 'Online'),
    ]

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    payment_status = models.CharField(max_length=10, choices=PAYMENT_STATUS, default='Unpaid')
    payment_method = models.CharField(max_length=10, choices=PAYMENT_METHOD, null=True, blank=True)
    total_amount = models.DecimalField(max_digits=100, decimal_places=2, default=0)

    def update_total(self):
        total = self.ordereditem_set.aggregate(total=Sum('total_price'))['total'] or 0
        self.total_amount = total
        self.save()


class OrderedItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    selling_price = models.DecimalField(max_digits=100, decimal_places=2, blank=True, null=True)
    total_price = models.DecimalField(max_digits=100, decimal_places=2, blank=True, null=True)
    profit_per_item = models.DecimalField(max_digits=100, decimal_places=2, blank=True, null=True)


class Profit(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    profit_amount = models.DecimalField(max_digits=100, decimal_places=2, default=0) 

    def __str__(self):
        return f"{self.order} ({self.profit_amount})"
    