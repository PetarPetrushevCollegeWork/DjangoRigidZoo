from django.contrib import admin
from .models import Ticket
# Register your models here.

class TicketAdmin(admin.ModelAdmin):
    list_display = ["user", "ticketType", "datePurchased", "dateStarting"]

admin.site.register(Ticket, TicketAdmin)