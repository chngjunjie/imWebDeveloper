from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
homefileUrls = 'homeintro'
lavaFileUrls = 'lava'
in_progressUrls = 'in_progress'

def home(request):
    return render(request, in_progressUrls + "/" + 'in_progress.html')

def contact(request):
    return render(request,  homefileUrls + "/" + 'generic.html')

def lavaHome(request):
    return render(request, in_progressUrls + "/in_progress.html")