# events/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('upcoming/', views.upcoming_events, name='upcoming_events'),
    # You can add more event-related URL patterns here
]
