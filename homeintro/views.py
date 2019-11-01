from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
homefileUrls = 'homeintro'
lavaFileUrls = 'lava'

def home(request):
    return render(request, homefileUrls + "/" + 'index.html')

def contact(request):
    return render(request,  homefileUrls + "/" + 'generic.html')

def lavaHome(request):
    return render(request, lavaFileUrls + "/index.html")