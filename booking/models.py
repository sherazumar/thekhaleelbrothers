from django.db import models
from django.utils import timezone


class Service(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Booking(models.Model):
    occasion = models.CharField(max_length=200)
    message = models.TextField(blank=True, null=True)
    date = models.DateField()
    time = models.TimeField()
    customer_name = models.CharField(max_length=100)
    customer_email = models.EmailField(null=True, blank=True)
    customer_phone = models.CharField(max_length=15)
    city_country = models.CharField(max_length=100, default='United Kingdom')
    number_of_guests = models.PositiveIntegerField(default=1)
    special_requests = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=100, default='Pending', choices=(('Pending', 'Pending'), ('Confirmed', 'Confirmed'), ('Cancelled', 'Cancelled')))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.customer_name} - {self.occasion} - {self.date} - {self.time}"
