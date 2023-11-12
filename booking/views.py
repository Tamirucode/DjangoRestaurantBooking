from django.shortcuts import render
from .models import Booking
from .forms import BookingForm




def get_booking_list(request):
    bookings = Booking.objects.all()

    context = {
        'bookings':bookings
    }
    return render(request, 'restaurant/booking_list.html', context)