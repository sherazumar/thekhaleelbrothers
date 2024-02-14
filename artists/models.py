from django.db import models

class Artist(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    # Add more fields as needed
