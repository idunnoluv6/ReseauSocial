from django.shortcuts import render

# Create your views here.

def Evenement (request) :
    return render (request, 'event.html')