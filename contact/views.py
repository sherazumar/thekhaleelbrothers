from django.shortcuts import render, redirect
from .models import Contact
from django.contrib import messages


def contact_view(request):
    if request.method == 'POST':
        contact = Contact(
            full_name=request.POST.get('full_name'),
            email=request.POST.get('email'),
            subject=request.POST.get('subject'),
            message=request.POST.get('message')
        )
        contact.save()
        messages.add_message(request, messages.SUCCESS, 'Thank you for your message! We will be in touch soon.')

        return redirect('contact')

    return render(request, 'contact/contact.html')
