# artists/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.artist_profile, name='artist_profile'),
]
