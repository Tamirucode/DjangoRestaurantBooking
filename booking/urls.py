
from django.urls import path
from booking import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.get_booking_list, name="get_booking_list"),
    
]
