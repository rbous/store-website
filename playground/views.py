from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def say_hello(request):
    return render(request, 'hello.html', {'name': 'Rayane'})

def home_page(request):
    return HttpResponse("<h1>Home page</h1>")