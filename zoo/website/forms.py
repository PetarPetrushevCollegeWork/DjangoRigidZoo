from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from .models import Ticket
from datetime import timedelta
from django import forms
from django.utils import timezone
from django.contrib.admin import widgets

class RegistrationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ["username", "password1", "password2"]

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ["dateStarting", "ticketType"]

        widgets = {
            'dateStarting': forms.DateInput(attrs={
                'type':'date',
                'class': 'form-control'
            })
        }