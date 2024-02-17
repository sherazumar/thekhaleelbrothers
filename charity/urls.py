from django.urls import path
from .views import charity_work_view

urlpatterns = [
    path('', charity_work_view, name='charity'),
]
