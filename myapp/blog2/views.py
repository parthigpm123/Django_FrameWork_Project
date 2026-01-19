from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
# Create your views here.

def sample_view(request):
      return HttpResponse("This is a sample view from blog2 app")
