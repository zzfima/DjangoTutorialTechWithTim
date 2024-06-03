from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(response):
    return HttpResponse("i am an index")


def about(response):
    return HttpResponse("i am an Django tutorial")
