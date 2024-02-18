from django.shortcuts import render
from .models import Nasheed


def nasheeds_list(request):
    nasheeds = Nasheed.objects.all()
    return render(request, 'nasheeds/nasheeds_list.html', {'nasheeds': nasheeds})
