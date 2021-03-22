from django.shortcuts import render,redirect
from travello.models import Destination

# Create your views here.

def destinations(request):
    dests = Destination.objects.all()
    return render(request,"destinations.html",{'dests':dests})


def offers(request):
    dests = Destination.objects.all()
    return render(request,"offers.html",{'dests':dests})

def desert(request):
    return render(request,"desert.html")

def fly(request):
    return render(request,"fly.html")

def water(request):
    return render(request,"water.html")


