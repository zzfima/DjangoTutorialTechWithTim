from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("about", views.about, name="about"),
    path("todolist/<int:id>", views.toDoList, name="toDoList"),
    path("item/<int:id>", views.item, name="item"),
]
