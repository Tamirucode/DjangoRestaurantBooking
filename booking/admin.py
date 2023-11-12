from django.contrib import admin
from.models import Booking

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):

    list_display = ('name', 'Number_of_persons', 'phone_number', 'booking_date_and_time')
    search_fields = ['name', 'phone_number']
    list_filter = ('name', 'booking_date_and_time')
   