from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField



class Booking(models.Model):
    """
    Class to represent booking model
    in database and for booking form.
    
    """
    
    name = models.CharField(max_length=20, null=False)
    
    Number_of_persons = models.PositiveIntegerField(
                            null=True,
                            validators=[MinValueValidator(1)])
    phone_number = PhoneNumberField(null=False, default='+44 7814985924')
    
    def validate_date(booking_date_and_time):
        """
        Function to validate date so that
        booking date and time should be in the future.
        """
        if booking_date_and_time < timezone.now():
            raise ValidationError("Date and Time cannot be in the past")
        
    booking_date_and_time = models.DateTimeField(
                                null=False,
                                blank=False,
                                validators=[validate_date] 
                               )
        
    
    class Meta:
        """
        Class container with metadata
        attached to the model.
        """
        
        unique_together = [ 'name', 'phone_number']
        
    
    def __str__(self):
        """
        Function to return object model
        bookings as string.
        """
        return f' User {self.name} has made a booking \
                for {self.Number_of_persons} persons\
                   for {self.booking_date_and_time }'
