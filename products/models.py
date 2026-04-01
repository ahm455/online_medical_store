from django.db import models

class Medicine(models.Model):
    name = models.CharField(max_length=30)
    potency = models.CharField(max_length=20)
    cost_price = models.DecimalField(max_digits=10, decimal_places=2)
    selling_price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    expiry_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.potency})"
