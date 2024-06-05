from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("base", views.base, name="base"),
    path("about", views.about, name="about"),
    path("todolist/<int:id>", views.toDoList, name="toDoList"),
    path("item/<int:id>", views.item, name="item"),
]
