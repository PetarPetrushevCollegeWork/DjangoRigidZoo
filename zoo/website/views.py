from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm
from django.contrib import messages
from .models import Ticket
from .forms import TicketForm
from .forms import HotelForm
from .models import HotelRoom
from django.shortcuts import get_object_or_404
# Create your views here.
def home(request):
    return render(request, 'webpages/home.html')

def animals(request):
    return render(request, 'webpages/animals.html')

@login_required
def buybasic(request):
    form = TicketForm()
    return render(request, 'webpages/buybasic.html', {"form": form})

@login_required
def buytour(request):
    form = TicketForm()
    return render(request, 'webpages/buytour.html', {"form": form})

@login_required
def buyyear(request):
    form = TicketForm()
    return render(request, 'webpages/buyyear.html', {"form": form})

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

@login_required
def buy(request):
    if request.method == "POST":
        form = TicketForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.save()
            return redirect("booked")
    return redirect("")

@login_required
def booked(request):
    return render(request, 'webpages/booked.html')

@login_required
def bookings(request):
    userTickets = Ticket.objects.filter(user_id=request.user)
    userHotelRooms = HotelRoom.objects.filter(user_id=request.user)
    return render(request, 'webpages/bookings.html', {"tickets": userTickets, "hotelRooms": userHotelRooms})

@login_required
def cancel(request, pk):
    context = get_object_or_404(Ticket, pk=pk)
    context.delete()
    return redirect("bookings")

@login_required
def cancelb(request, pk):
    context = get_object_or_404(HotelRoom, pk=pk)
    context.delete()
    return redirect("bookings")

def hotel(request):
    return render(request, 'webpages/hotel.html')

@login_required
def hotelbook(request):
    if request.method == "POST":
        form = HotelForm(request.POST)
        if(form.is_valid()):
            form = form.save(commit=False)
            form.user = request.user
            form.save()
            return redirect("booked")
        else:
            return redirect("bookhotel")
    else:
        form = HotelForm()
        return render(request, 'webpages/bookhotel.html', {"form": form})