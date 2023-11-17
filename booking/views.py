from django.shortcuts import render, redirect, get_object_or_404
from .models import Booking
from .forms import BookingForm
from django.contrib import messages


def home(request):
    return render(request, 'booking/home.html')
  

def about(request):
    return render(request, 'booking/about.html')


def menu(request):
    return render(request, 'booking/menu.html')


def contact(request):
    
    if request.method == "POST":
        messages.success(request, "Thanks, we have received your message!")
    return render(request, 'booking/contact.html')


def get_booking_list(request):
    
    context = {}
    user = request.user
    bookings= Booking.objects.filter(name=user)
    if bookings:
        return render(request, 'booking/booking_list.html', locals())
    else:
        messages.error(request, "Sorry you have no booked table!", context)
        return render(request, 'booking/booking_list.html', context)


def add_booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST or None)
        if form.is_valid():
            booking = form.save()
            booking.user = request.user
            booking.save()
            return render(request, 'booking/booking_confirmation.html', locals())
        else:
            return render(request, 'booking/add_booking.html',{'form': form} )
    form = BookingForm()
    context = {
        'form': form
    }
    return render(request, 'booking/add_booking.html', context)


def edit_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            booking = form.save()
            booking.user = request.user
            booking.save()
            return render(request, 'booking/booking_confirmation.html', locals())
        else:
            return render(request, 'booking/edit_booking.html',{'form': form} )
    form = BookingForm(instance=booking)
    context = {
        'form': form
    }
    return render(request, 'booking/edit_booking.html', context)


def delete_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    booking.delete()
    return redirect('mybooking')