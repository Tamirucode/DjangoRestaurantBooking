from django.test import TestCase
from.models import Booking
# Create your tests here.

class TestViews(TestCase):

    def test_home(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'booking/home.html')
    
    def test_about(self):
        response = self.client.get('/about')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'booking/about.html')

    def test_menu(self):
        response = self.client.get('/menu')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'booking/menu.html')

    def test_contact(self):
        response = self.client.get('/contact')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'booking/contact.html')

    def test_get_booking_list(self):
        response = self.client.get('/mybooking')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'booking/booking_list.html')

    def test_get_add_booking_page(self):
        response = self.client.get('/add')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'booking/add_booking.html')


    def test_get_edit_booking_page(self):
        booking = Booking.objects.create(name='Test Booking')
        response = self.client.get(f'/edit/{booking.id}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'booking/edit_booking.html')


    def test_can_add_booking(self):
        response = self.client.post('/add', {'name': 'Test Added Booking'})
        self.assertTemplateUsed('booking/booking_confirmation.html')

    
    def test_can_delete_booking(self):
        booking = Booking.objects.create(name='Test Booking')
        response = self.client.get(f'/delete/{booking.id}')
        self.assertRedirects(response, '/mybooking')
        existing_bookings = Booking.objects.filter(id=booking.id)
        self.assertEqual(len(existing_bookings), 0)


    def test_can_edit_booking(self):
        booking = Booking.objects.create(name='Test Booking')
        response = self.client.post(f'/edit/{booking.id}', {'name': 'Updated Booking'})
        self.assertTemplateUsed('booking/booking_confirmation.html')
        updated_booking = Booking.objects.get(id=booking.id)
        self.assertTrue(updated_booking.name, 'Updated Booking')