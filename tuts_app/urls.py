from django.contrib import admin
from django.urls import path
from tuts_app import views


urlpatterns = [
    path('', views.index,name='index'),
    path('about', views.about,name='about'),
    path('contact', views.contact,name='contact'),
    path('login', views.loginuser,name='login'),
    path('logout', views.logoutuser,name='logout'),
]
