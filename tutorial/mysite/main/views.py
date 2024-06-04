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
        return HttpResponse("ToDoList id {} is {}".format(id, ToDoList.objects.get(id=id).name))
    except:
        return HttpResponse("id {} not found".format(id))
