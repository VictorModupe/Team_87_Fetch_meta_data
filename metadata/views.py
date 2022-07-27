from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def index(request):
    return HttpResponse("Hello Index")


def login(request):
    return HttpResponse("Hello login")


def register(request):
    return HttpResponse("Hello register")


def metadata(request):
    return HttpResponse("Hello metadata")


def user(request):
    return HttpResponse("Hello metadata")
