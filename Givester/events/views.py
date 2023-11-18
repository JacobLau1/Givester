from django.shortcuts import render, HttpResponse

# Create your views here.
def events(request):
    #return HttpResponse("Hello, world. You're at the polls index.")
    return render(request, "events.html")

def apply(request):
    #return HttpResponse("Hello, world. You're at the polls index.")
    return render(request, "apply.html")