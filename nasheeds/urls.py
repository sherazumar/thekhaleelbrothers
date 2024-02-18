from django.urls import path
from . import views

urlpatterns = [
    path('', views.nasheeds_list, name='nasheeds_list'),
]
