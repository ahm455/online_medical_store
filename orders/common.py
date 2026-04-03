from django.db import models

class Create_Update_Time(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Payment_Choices(models.Model):
    PAYMENT_STATUS = [
        ('Paid', 'Paid'),
        ('Unpaid', 'Unpaid'),
    ]

    class Meta:
        abstract = True

class Status_choices(models.Model): 
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Shipped', 'Shipped'),
        ('Delivered', 'Delivered'),
    ]

    class Meta:
        abstract = True


class Payment_methods(models.Model):
    PAYMENT_METHOD = [
        ('Cash', 'Cash'),
        ('Card', 'Card'),
        ('Online', 'Online'),
    ]
    class Meta:
            abstract = True