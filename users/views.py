# users/views.py

from django.shortcuts import render, redirect

def register(request):
    # Registration logic here
    return render(request, 'users/register.html')

def login_user(request):
    # Login logic here
    return render(request, 'users/login.html')

def logout_user(request):
    # Logout logic here
    return redirect('homepage')

def profile(request):
    # Profile viewing logic here
    return render(request, 'users/profile.html')
