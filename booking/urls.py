# booking/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('book-event/', views.book_event, name='book_event'),
]
