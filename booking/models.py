from django.utils import timezone

from django.db import models

class Service(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)  # Optional

    def __str__(self):
        return self.name


class Booking(models.Model):
    date = models.DateField()
    time = models.TimeField()
    customer_name = models.CharField(max_length=100)
    customer_email = models.EmailField()
    customer_phone = models.CharField(max_length=15)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)  # Link to Service model
    number_of_guests = models.PositiveIntegerField(default=1)
    special_requests = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=100, default='Pending', choices=(('Pending', 'Pending'), ('Confirmed', 'Confirmed'), ('Cancelled', 'Cancelled')))
    created_at = models.DateTimeField(auto_now_add=True, default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.customer_name} - {self.service.name} - {self.date} - {self.time}"
