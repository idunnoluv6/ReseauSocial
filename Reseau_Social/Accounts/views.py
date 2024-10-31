from django.shortcuts import render

# Create your views here.

def connexion (request) :
    return render (request, 'form-login.html')

def inscription (request) :
    return render (request, 'form-register.html')