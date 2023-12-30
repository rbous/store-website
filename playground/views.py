from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import ToDoList, Item
from .forms import CreateNewList, SearchForList

from django.views.decorators.csrf import csrf_exempt

# Create your views here.


def say_hello(request):
    return render(request, 'hello.html', {'name': 'Rayane'})


def home_page(request):
    return render(request, "home.html", {})


def index(request, id):
    ls = ToDoList.objects.get(id=id)

    if request.method == "POST":
        print(request.POST)
        if request.POST.get("save"):
            for item in ls.item_set.all():
                if request.POST.get("c" + str(item.id)) == "clicked":
                    item.complete = True
                else:
                    item.complete = False

                item.save()

        elif request.POST.get("newItem"):
            txt = request.POST.get("new")

            if len(txt) > 2:
                ls.item_set.create(text=txt, complete=False)
            else:
                print("invalid")

    return render(request, "list.html", {"ls": ls})


def create(request):
    if request.method == 'POST':
        form = CreateNewList(request.POST)

        if form.is_valid():
            n = form.cleaned_data['name']
            ls = ToDoList.objects.filter(name=n)

            if ls:
                t = ls[0]
            else:
                t = ToDoList(name=n)
                t.save()

        return HttpResponseRedirect("/%i" %t.id)

    else:
        form = CreateNewList()
    return render(request, "create.html", {'form': form})


def search(request):

    if request.method == 'GET':
        form = SearchForList(request.GET)

        if str(form)[177:181] == "true":
            form = SearchForList()
            return render(request, "search.html", {'exists': None, 'form': form})

        if form.is_valid():
            n = form.cleaned_data['name']

        else:
            n = ''

        todolist = ToDoList.objects.filter(name=n)

        if todolist:

            return HttpResponseRedirect("/%i" % todolist[0].id)

        return render(request, "search.html", {'exists': False, 'form': form})


