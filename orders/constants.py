from django.db import models
from django.utils.translation import gettext_lazy as _

class PaymentMethodChoices(models.TextChoices):
    CASH = "CA", _("Cash")
    CARD = "CR", _("Card")
    ONLINE = "ONL", _("Online")

class PaymentStatusChoices(models.TextChoices):
    PAID = "PA", _("Paid")
    UNPAID = "UP", _("Unpaid")

class OrderStatusChoices(models.TextChoices):
    PENDING = "PD", _("Pending")
    SHIPPED = "SH", _("Shipped")
    DELIVERED="DEL",_("Delivered")