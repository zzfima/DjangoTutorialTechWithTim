from django.shortcuts import render
from django.http import HttpResponse
from main.models import ToDoList, Item


# Create your views here.
def index(response):
    return HttpResponse("i am an index")


def about(response):
    return HttpResponse("i am an Django tutorial")


def toDoList(response, id):
    try:
        return HttpResponse(
            "ToDoList id={}. Its name={}".format(id, ToDoList.objects.get(id=id).name)
        )
    except:
        return HttpResponse("id={} not found".format(id))


def item(response, id):
    try:
        i = Item.objects.get(id=id)
        return HttpResponse(
            "Item id={}. Its text={}. Parent ToDoList id={} ".format(id, i.text, i.todoList_id)
        )
    except:
        return HttpResponse("id={} not found".format(id))


def home(response):
    return render(response, "main/home.html", {"name": "home page"})

def listing(response, id):
    ls = ToDoList.objects.get(id=id)
    return render(response, "main/listing.html", {"name": "home page", "ls": ls})

def base(response):
    return render(response, "main/base.html", {"name": "base page"})
