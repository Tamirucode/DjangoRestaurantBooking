
from django.urls import path
from booking import views
urlpatterns = [
    
    path("", views.get_booking_list, name='home'),
    path("mybooking", views.get_booking_list, name='mybooking'),
    path('add', views.add_booking, name='add'),
    
]
