from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("<h1> Мистер Django передает привет (00)</h1>")

def data(request):
    return HttpResponse("<h1> Я правильно понял домашнее задание? @_@ </h1>")

def test(request):
    return HttpResponse("<h1>  чего тестируем?=_= </h1>")
