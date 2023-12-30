from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoList, Item

# Create your views here.


def say_hello(request):
    return render(request, 'hello.html', {'name': 'Rayane'})


def home_page(request):
    return render(request, "home.html", {})


def index(request):
    return render(request, "base.html", {})
