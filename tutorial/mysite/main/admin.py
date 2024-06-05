from django.contrib import admin
from main.models import Item, ToDoList

# Register your models here.
admin.site.register(ToDoList)
admin.site.register(Item)
