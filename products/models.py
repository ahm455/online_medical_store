from django.db import models
from orders.common import CreateUpdateTime
from django.core.validators import MinValueValidator

class Medicine(CreateUpdateTime):
    name = models.CharField(max_length=30)
    potency = models.CharField(max_length=20)
    cost_price = models.DecimalField(max_digits=10, decimal_places=2)
    selling_price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField(validators=[MinValueValidator(1)])
    expiry_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.potency})"

