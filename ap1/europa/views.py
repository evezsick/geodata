from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def id(request):
    return render (request, "id.html")

def georgia(request):
    return render (request, "georgia.html")

def paisdgales(request):
    return render (request, "paisdgales.html")

def russia2(request):
    return render (request, "russia2.html")
