from django.contrib.auth import views as auth_views
"""
URL configuration for zoo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name=""),
    path('animals', views.animals, name="animals"),
    path("login", auth_views.LoginView.as_view(), name="login"),
    path("logout", auth_views.LogoutView.as_view(), name="logout"),
    path("buy", views.buy, name='buy'),
    path("buy/basic", views.buybasic, name='buybasic'),
    path("buy/tour", views.buytour, name='buytour'),
    path("buy/year", views.buyyear, name='buyyear'),
    path("register", views.register, name="register"),
    path("booked", views.booked, name="booked"),
    path("bookings", views.bookings, name="bookings"),
    path("cancel-ticket/<int:pk>", views.cancel, name="cancel"),
    path("hotel", views.hotel, name="hotel"),
    path("hotel/book", views.hotelbook, name="bookhotel"),
    path("cancel-booking/<int:pk>", views.cancelb, name="cancel"),
]
