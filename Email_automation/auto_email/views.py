from django.shortcuts import render
from django.http import HttpResponse
from . task import test_func
# Create your views here.

def home(request):
    test_func.delay()
    return HttpResponse('<h1> Well come to email automation....</h1>')