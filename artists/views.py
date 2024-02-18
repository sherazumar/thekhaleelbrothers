from django.shortcuts import render
from .models import Artist


def artist_profile(request):
    artists = Artist.objects.all()
    return render(request, 'artists/artist_profile.html', {'artists': artists})


