from decimal import Decimal

from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

# Create your models here.

class Ticket(models.Model):
    
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name="zoo_tickets"
    )
    ticketType = models.CharField(
        max_length=10,
        choices=[("basic","Basic"), ("tour","Tour"), ("year","Yearly pass")],
        default='basic',
    )
    datePurchased = models.DateTimeField(auto_now_add=True)
    dateStarting = models.DateTimeField(blank=True)