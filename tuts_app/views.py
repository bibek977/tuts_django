from django.shortcuts import render,redirect
from tuts_app.models import Candle
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib import messages

def index(request):
    candles=Candle.objects.all()
    # print(candles)
    params = {'product' : candles, 'total' : len(candles)}
    if request.user.is_authenticated:
        return render(request, "index.html",params)
    else:
        return redirect('/login')

def about(request):
    candles=Candle.objects.all()
    # print(candles)
    params = {'product' : candles, 'total' : len(candles)}
    return render(request, "about.html",params)
    
def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        desc = request.POST.get('desc')
        price = request.POST.get('price')
        image = request.POST.get('image')
        candle = Candle(name = name, desc=desc, price=price, image=image)
        candle.save()

        messages.success(request, f'{name} details updated.')

    return render(request, "contact.html")

def loginuser(request):
    if request.method== "POST":
        name=request.POST.get('name')
        pw = request.POST.get('pw')
        user = authenticate(username=name, password=pw)
        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            return render(request, 'login.html')
    return render(request, "login.html")

def logoutuser(request):
    logout(request)
    return render(request, "login.html")

# Create your views here.
