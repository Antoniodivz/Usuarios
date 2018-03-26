from django.shortcuts import render, HttpResponse
from django.contrib.auth.models import User

def home(request):
    numbers = [1,2,3,4,5]
    name = 'Marco Antonio'

    args = {'myName': name, 'numbers': numbers}

    return render(request, 'accounts/home.html', args)

def profile(request):
    args = {'user': request.user}
    return render(request, 'accounts/profile.html',args)