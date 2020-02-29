from django.shortcuts import render
from django.http import HttpResponse


def login(request):
    return HttpResponse("Here will be the login page")

def register(request):
    return HttpResponse("Here will be the register page")

def user(request):
    return HttpResponse("Here user will configure its account")