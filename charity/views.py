from django.shortcuts import render
from .models import CharityWork
# Create your views here.

def charity_work_view(request):
    charity_works = CharityWork.objects.all().order_by('-date')
    return render(request, 'charity/charity_work.html', {'charity_works': charity_works})
