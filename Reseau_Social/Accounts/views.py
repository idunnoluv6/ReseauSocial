from django.shortcuts import render

# Create your views here.

def connexion (request) :
    return render (request, 'Accounts/form-login.html')

def inscription (request) :
    return render (request, 'Accounts/form-register.html')