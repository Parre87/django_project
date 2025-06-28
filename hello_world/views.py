# from django.shortcuts import render
# from django.http import HttpResponse /only for me for testing purposes/

from django.shortcuts import render, redirect
from .models import Destination, Booking
from .forms import BookingForm
from django.contrib.auth.decorators import login_required

 

# Create your views here.
# def index(request):
    # return HttpResponse("Hello, world!") /# only for me for testing purposes/

def home(request):
    return render(request, 'home.html')

def list_destinations(request):
    destinations = Destination.objects.all()
    return render(request, 'list_destinations.html', {'destinations': destinations})

@login_required
def book_destination(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.save()
            return redirect('dashboard')
    else:
        form = BookingForm()
    return render(request, 'booking_form.html', {'form': form})

@login_required
def dashboard(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'dashboard.html', {'bookings': bookings})
