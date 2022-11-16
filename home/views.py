from django.shortcuts import render, HttpResponse

import requests
from django.shortcuts import render, redirect
from bs4 import BeautifulSoup as BSoup


def index(request):
    return render(request, 'index.html')

def localnews(request):
    return render(request, 'localnews.html')

def currentnews(request):
    return render(request, 'currentnews.html')

def sport(request):
    return render(request, 'sport.html')

def businessnews(request):
    return render(request, 'businessnews.html')
