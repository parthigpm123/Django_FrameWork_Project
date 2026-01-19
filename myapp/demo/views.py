from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def gm(request):
      return HttpResponse("GOOD MORNING")

def ga(request):
      return HttpResponse("GOOD AFTERNOON")

def ge(request):
      return HttpResponse("GOOD EVENING")