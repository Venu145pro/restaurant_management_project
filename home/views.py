
from django.conf import settings
from django.shortcuts import render

def homepage(request):
    context = {
        'restaurant_name': settings.RESTAURANT_NAME
    }
    return render(request, 'index.html', context)
