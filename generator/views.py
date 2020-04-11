from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def home(request):
    return render(request, 'generator/home.html')

def password(request):
    lowerletters = list('abcdefghijklmnopqrstuvwxyz')
    password = ''
    length = int(request.GET.get('length', 12))
    if request.GET.get('uppercase'):
        lowerletters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('special'):
        lowerletters.extend(list('!@#$%^&*()'))

    if request.GET.get('numbers'):
        lowerletters.extend(list('1234567890'))

    for i in range(length):
        password += random.choice(lowerletters)
    return render(request, 'generator/password.html', {'password': password})