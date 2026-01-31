from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
import logging
from .models import Post
from django.http import Http404

# Create your views here.
#static demo data
# posts = [
#             {'id':1,'title':'post 1', 'content':'content for post 1'},
#             {'id':2,'title':'post 2', 'content':'content for post 2'},
#             {'id':3,'title':'post 3', 'content':'content for post 3'},
#             {'id':4,'title':'post 4', 'content':'content for post 4'}
     
#       ]

def index(request):
      blog_title = "Latest Posts"
      #Getting data from model
      Posts=Post.objects.all()

      return render(request,'index.html',{'blog_title':blog_title,'posts':Posts})
#Dynamic URL handling with parameter
def detail(request, slug):
      #static data
      # post = next((item for item in Posts if item['id'] == int(post_id)), None)
      try:
      #Getting data from model by post id
          post = Post.objects.get(slug=slug)
      except Post.DoesNotExist:
            raise Http404("Post does not exist!!")  
     
      # logger = logging.getLogger('TestLogger')
      # logger.debug(f"post variable is {post}")
      return render(request,'detail.html',{'post': post})
 

def old_url_redirect(request, post_id):
      return redirect('new_url')

def new_url(request):
      return HttpResponse("This is the new URL page.")


