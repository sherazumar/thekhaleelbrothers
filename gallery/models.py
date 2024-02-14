from django.db import models

class GalleryImage(models.Model):
    objects = None
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='gallery/')
    description = models.TextField(blank=True)
    # Add other fields as needed

    def __str__(self):
        return self.title
