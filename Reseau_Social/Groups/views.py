from django.shortcuts import render

# Create your views here.

def Groups (request):
    return render(request,'groups.html')