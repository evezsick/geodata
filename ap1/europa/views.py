from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render (request, "index.html")

def georgia(request):
    return render (request, "georgia.html")

def paisdgales(request):
    return render (request, "paisdgales.html")
