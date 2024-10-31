from django.shortcuts import render

# Create your views here.

def Pages (request):
    return render(request, 'pages.html')