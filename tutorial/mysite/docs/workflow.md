# Django

## What is Django?

Django is a Python framework that makes it easier to create web sites using Python.
Django follows the MVT design pattern (Model View Template).

- Model - The data you want to present, usually data from a database.
- View - A request handler that returns the relevant template and content - based on the request from the user.
- Template - A text file (like an HTML file) containing the layout of the web page, with logic on how to display the data.

![alt text](image.png)

## development steps

- create venv: python -m venv venv
- activate venv: .\venv\Scripts\activate
- install Django: pip install django
- create Django project: django-admin startproject mysite
- testing project (port can be added at the end of command): python .\mysite\manage.py runserver
- django application.
  - A project refers to the entire application and all its parts.
  - An app refers to a submodule of the project
- creating application named 'main':
  - cd .\mysite
  - python manage.py startapp main
- starting modify views.py. Django views are Python functions that takes http requests and returns http response, like HTML documents.
-
