from django.shortcuts import render
from .models import *

def event_home(request):
    events = Event.objects.all()
    context = {
        'title':'ETV | Events',
        'events': events,
    }
    return render(request, "events-home.html", context)

def golf(request):
    context = {
        'title':'ETV | Power Swing Classic',
    }
    return render(request, "golf.html", context)
