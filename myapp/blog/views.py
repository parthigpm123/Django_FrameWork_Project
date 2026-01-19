from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
import logging

# Create your views here.
posts = [
            {'id':1,'title':'post 1', 'content':'content for post 1'},
            {'id':2,'title':'post 2', 'content':'content for post 2'},
            {'id':3,'title':'post 3', 'content':'content for post 3'},
            {'id':4,'title':'post 4', 'content':'content for post 4'}
      
      ]

def index(request):
      blog_title = "Parthiban Blog"

      return render(request,'index.html',{'blog_title':blog_title,'posts':posts})
#Dynamic URL handling with parameter
def detail(request, post_id):
      post = next((item for item in posts if item['id'] == int(post_id)), None)
      logger = logging.getLogger('TestLogger')
      logger.debug(f"post variable is {post}")
      return render(request,'detail.html',{'post':post})
 

def old_url_redirect(request, post_id):
      return redirect('new_url')

def new_url(request):
      return HttpResponse("This is the new URL page.")

