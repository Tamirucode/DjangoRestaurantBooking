from django.test import TestCase
from.forms import BookingForm
# Create your tests here.

class TestBookingForm(TestCase):
    def test_booking_name_is_required(self):
        form=BookingForm({"name":""})
        self.assertFalse(form.is_valid())
        self.assertIn("name",form.errors.keys())
        self.assertEqual(form.errors['name'][0], 'This field is required.')

    def test_fields_are_explicit_in_form_metaclass(self):
        form = BookingForm()
        self.assertEqual(form.Meta.fields, ['name', 'phone_number', 'Number_of_persons', 'booking_date_and_time'])