from django.http import HttpResponseNotFound
from django.shortcuts import render
from .models import *


def index(request):
    return render(request, 'planner/index.html')


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
