from django.shortcuts import render, HttpResponse
from .models import Event
from django.utils.timezone import datetime

# Create your views here.
def events(request):
    #return HttpResponse("Hello, world. You're at the polls index.")
    items = Event.objects.all()
    date = datetime.date(datetime.now())
    return render(request, "events.html", {'event': items , 'date': date})

def apply(request,data):
    #return HttpResponse("Hello, world. You're at the polls index.")
    #items = Event.objects.get(data)

    item = Event.objects.get(pk=data)
    

    return render(request, "apply.html", {'event': item })

