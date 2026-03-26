from django.db import models

class Medicine(models.Model):
    medicine_name = models.CharField(max_length=100)
    potency = models.CharField(max_length=20)
    cost_price = models.DecimalField(max_digits=10, decimal_places=2)
    selling_price = models.DecimalField(max_digits=10, decimal_places=2)
    expiry_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.medicine_name} ({self.potency})"


class Stock(models.Model):
    medicine = models.OneToOneField(Medicine, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return f"{self.medicine.medicine_name} - {self.quantity} units"