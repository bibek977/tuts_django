from django.shortcuts import render
from tuts_app.models import Candle

def index(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")
    
def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        desc = request.POST.get('desc')
        candle = Candle(name = name, desc=desc)
        candle.save()
    return render(request, "contact.html")

# Create your views here.
