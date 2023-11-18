from django.test import TestCase
from .models import Booking
from django.utils import timezone

class TestModels(TestCase):

    def test_name_defaults_to_false(self):
        booking = Booking.objects.create(name='Test Booking')
        self.assertTrue(booking.name)

    def test_booking_string_method_returns_name(self):
        booking = Booking.objects.create(name='Test Booking')
        self.assertTrue(str(booking), 'Test booking')

    def test_booking_date_and_time_returns_future(self):
        booking = Booking.objects.create(name='Test Booking')
        booking_date_and_time= timezone.now()
        self.assertTrue(booking_date_and_time, 'Test Booking')
