from django.shortcuts import render, redirect, get_object_or_404
from .models import Booking
from .forms import BookingForm

def home(request):
    return render(request, 'restaurant/home.html')
  

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
            ##return redirect('get_booking_list')
            return render(request, 'restaurant/booking_confirmation.html', locals())
        else:
            return render(request, 'restaurant/add_booking.html',{'form': form} )
    form = BookingForm()
    context = {
        'form': form
    }
    return render(request, 'restaurant/add_booking.html', context)

def edit_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            return render(request, 'restaurant/booking_confirmation.html', locals())
        else:
            return render(request, 'restaurant/edit_booking.html',{'form': form} )
    form = BookingForm(instance=booking)
    context = {
        'form': form
    }
    return render(request, 'restaurant/edit_booking.html', context)

    def delete_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    booking.delete()
    return redirect('mybooking')