from django.shortcuts import render
from django.urls import path
from django.contrib import admin

def home(request):
    return render(request,'home.html')
def habilidades(request):
    return render(request, 'habilidades.html')
def github(request):
    return render(request, 'git hub.html')
def pretencao(request):
    return render(request,'pretencao.html')