from django.shortcuts import render

# Create your views here.

def Fundraiser (request):
    return render(request, 'funding.html')