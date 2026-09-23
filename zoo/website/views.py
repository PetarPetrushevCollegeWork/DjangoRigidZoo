from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm
from django.contrib import messages
from .models import Ticket
from .forms import TicketForm
from django.shortcuts import get_object_or_404
# Create your views here.
def home(request):
    return render(request, 'webpages/home.html')

def animals(request):
    return render(request, 'webpages/animals.html')

@login_required
def buybasic(request):
    if request.method == "POST":
        pass
    else:
        form = TicketForm()
    return render(request, 'webpages/buybasic.html', {"form": form})

def register(request):
    if request.user.is_authenticated:
        return redirect("home")
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your account is ready. Please sign in.")
            return redirect("login")
    else:
        form = RegistrationForm()
    return render(request, "registration/register.html", {"form": form})