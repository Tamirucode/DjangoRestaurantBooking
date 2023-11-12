
from django.urls import path
from booking import views
urlpatterns = [
    
    path("", views.get_booking_list, name='home'),
    
]
