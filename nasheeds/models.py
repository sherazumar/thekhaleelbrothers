from django.db import models


class Nasheed(models.Model):
    title = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title
