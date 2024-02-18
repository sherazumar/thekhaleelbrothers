from django.urls import path
from .views import book_event, booking_success

urlpatterns = [
    path('', book_event, name='book_event'),
    path('success/<str:customer_name>/<str:booking_date>/<str:booking_time>/', booking_success, name='booking_success'),
]
