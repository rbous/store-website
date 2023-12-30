from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoList, Item

# Create your views here.


def say_hello(request):
    return render(request, 'hello.html', {'name': 'Rayane'})


def home_page(request):
    return render(request, "home.html", {})


def index(request, id):
    ls = ToDoList.objects.get(id=id)
    return render(request, "list.html", {"ls": ls})
