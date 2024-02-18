# booking/views.py
from django.shortcuts import render

def services_view(request):
    # Add any context data you want to pass to the template
    context = {
        'additional_info': "Nasheeds for all occasions including weddings, aqeeqah events, and all Islamic programmes."
    }
    return render(request, 'booking/services.html', context)
