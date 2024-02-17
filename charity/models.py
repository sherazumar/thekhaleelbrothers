from django.db import models

class CharityWork(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='charity/images/')
    date = models.DateField()

    def __str__(self):
        return self.title
