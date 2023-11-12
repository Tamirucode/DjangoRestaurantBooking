from django.shortcuts import render
from .models import Booking
from .forms import BookingForm


def get_booking_list(request):
    bookings = Booking.objects.all()

    context = {
        'bookings':bookings
    }
    return render(request, 'restaurant/booking_list.html', context)

def add_booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('get_booking_list')
        else:
            return render(request, 'reservation/add_booking.html',{'form': form} )
    form = BookingForm()
    context = {
        'form': form
    }
    return render(request, 'reservation/add_booking.html', context)

