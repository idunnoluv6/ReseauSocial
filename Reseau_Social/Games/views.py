from django.shortcuts import render

# Create your views here.
def Games (request):
    return render(request, 'games.html')