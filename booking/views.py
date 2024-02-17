# booking/views.py
from django.shortcuts import redirect, render
from .models import Booking, Service
from django.http import HttpResponse


def book_event(request):
    if request.method == 'POST':
        # Extract form data
        customer_name = request.POST.get('customer_name')
        customer_email = request.POST.get('customer_email')
        customer_phone = request.POST.get('customer_phone')
        service_type = request.POST.get('service')
        number_of_guests = request.POST.get('number_of_guests')
        special_requests = request.POST.get('special_requests')

        # Fetch the Service object based on the service type selected
        service = Service.objects.get(name=service_type)

        # Create and save the new booking
        booking = Booking(
            customer_name=customer_name,
            customer_email=customer_email,
            customer_phone=customer_phone,
            service=service,
            number_of_guests=number_of_guests,
            special_requests=special_requests,
            date=request.POST.get('date'),  # Ensure you have a date field in your form
            time=request.POST.get('time'),  # Ensure you have a time field in your form
        )
        booking.save()

        # Redirect or show a success message
        return HttpResponse(
            "Booking successful!")  # For simplicity, you might want to redirect to a success page or show a message
    else:
        # Display the form
        services = Service.objects.all()
        return render(request, 'booking/book_event.html', {'services': services})
