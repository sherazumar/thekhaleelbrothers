# booking/models.py
from django.db import models

class Booking(models.Model):
    date = models.DateField()
    time = models.TimeField()
    customer_name = models.CharField(max_length=100)
    # Add more fields as necessary
