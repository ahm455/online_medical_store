from django.db import models

class CreateUpdateTime(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class choices:
    payment_method = (
        ('cash', "cash"),
        ('card', "card"),
        ('online', "online"),
    )

    payment_status = (
        ('paid', "paid"),
        ('unpaid', "unpaid")
    )
    status = (
        ('pending', "pending"),
        ('shipped', "shipped"),
        ('Delivered', "delivered"),
    )