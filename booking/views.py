from django.shortcuts import redirect, render
from django.urls import reverse
from .models import Booking
from django.http import HttpResponse


def book_event(request):
    if request.method == 'POST':
        # Extract form data
        occasion = request.POST.get('occasion')
        message = request.POST.get('message')
        city_country = request.POST.get('city_country')
        customer_name = request.POST.get('customer_name')
        customer_email = request.POST.get('customer_email')
        customer_phone = request.POST.get('customer_phone')
        date = request.POST.get('service_date')
        time = request.POST.get('service_time')

        # Create and save the new booking without the service object
        booking = Booking(
            occasion=occasion,
            message=message,
            city_country=city_country,
            customer_name=customer_name,
            customer_email=customer_email,
            customer_phone=customer_phone,
            date=date,
            time=time,
        )
        booking.save()

        # Redirect or show a success message
        return redirect(reverse('booking_success', kwargs={
            'customer_name': customer_name,
            'booking_date': date,
            'booking_time': time,
        }))
    else:
        # Display the form
        # Assuming services selection is disabled for now
        return render(request, 'booking/book_event.html')


def booking_success(request, customer_name, booking_date, booking_time):
    return render(request, 'booking/booking_success.html', {
        'customer_name': customer_name,
        'booking_date': booking_date,
        'booking_time': booking_time
    })