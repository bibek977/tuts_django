from django.shortcuts import render,redirect
from tuts_app.models import Candle
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib import messages

def index(request):
    if request.user.is_authenticated:
        return render(request, "index.html")
    else:
        return redirect('/login')

def about(request):
    return render(request, "about.html")
    
def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        desc = request.POST.get('desc')
        candle = Candle(name = name, desc=desc)
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
