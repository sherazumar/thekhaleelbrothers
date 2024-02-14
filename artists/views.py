# artists/views.py

from django.shortcuts import render

def artist_profile(request):
    # You might want to pass artist data to the template
    return render(request, 'artists/profile.html')
