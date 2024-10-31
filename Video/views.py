from django.shortcuts import render

# Create your views here.

def Video (request) :
    return render (request, 'Video.html')