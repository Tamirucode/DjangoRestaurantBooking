from django import forms
from .models import Booking
from django.forms import  widgets


class BookingForm(forms.ModelForm):
    """
    Class to construct booking form from the model.
    """
    class Meta:
        """
        Add form inputs from the model items as form fields.
        """
        model = Booking
        fields = ['name', 'phone_number', 'Number_of_persons', 'booking_date_and_time']
        widgets = {
            'booking_date_and_time': widgets.DateTimeInput(attrs={'type': 'datetime-local'})
        }

   