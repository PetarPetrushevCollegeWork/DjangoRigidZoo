from datetime import timedelta
from django import forms
from django.contrib.admin import widgets
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.utils import timezone
from .models import Ticket
from .models import HotelRoom


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
                'type': 'date',
                'class': 'form-control'
            })
        }

    def clean_dateStarting(self):
        date_starting = self.cleaned_data.get("dateStarting")

        if date_starting:
            # Extract just the .date() part whether it's datetime or date
            val_date = getattr(date_starting, 'date', lambda: date_starting)()
            if val_date < timezone.localdate():
                raise ValidationError("Date cannot be in the past.")

        return date_starting

class HotelForm(forms.ModelForm):
    class Meta:
        model = HotelRoom
        fields = ["roomSize", "dateStarting", "dateEnding"]

        widgets = {
            "dateStarting": forms.DateInput(
                attrs={"type": "date", "class": "form-control"}
            ),
            "dateEnding": forms.DateInput(
                attrs={"type": "date", "class": "form-control"}
            ),
        }

    def clean_dateStarting(self):
        date_starting = self.cleaned_data.get("dateStarting")

        if date_starting:
            # If date_starting is a datetime, extract its date part
            val_date = (
                date_starting.date()
                if hasattr(date_starting, "date")
                else date_starting
            )
            if val_date < timezone.localdate():
                raise ValidationError("Date cannot be in the past.")

        return date_starting

    def clean(self):
        cleaned_data = super().clean()
        date_starting = cleaned_data.get("dateStarting")
        date_ending = cleaned_data.get("dateEnding")

        if date_starting and date_ending:
            # Extract date component for both if they are datetimes
            start_val = (
                date_starting.date()
                if hasattr(date_starting, "date")
                else date_starting
            )
            end_val = (
                date_ending.date()
                if hasattr(date_ending, "date")
                else date_ending
            )

            if end_val < start_val:
                self.add_error(
                    "dateEnding",
                    "Ending date cannot be before starting date.",
                )

        return cleaned_data