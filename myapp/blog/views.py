from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
import logging
from .models import Post
from django.http import Http404
from django.core.paginator import Paginator
from .forms import ContactForm

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
      all_Posts=Post.objects.all()
      
      #pagination
      paginator = Paginator(all_Posts, 5)
      page_number = request.GET.get('page') 
      page_obj = paginator.get_page(page_number)
      
      

      return render(request,'index.html',{'blog_title':blog_title, 'page_obj': page_obj})
#Dynamic URL handling with parameter
def detail(request, slug):
      #static data
      # post = next((item for item in Posts if item['id'] == int(post_id)), None)
      try:
      #Getting data from model by post id
          post = Post.objects.get(slug=slug)
          related_posts = Post.objects.filter(category=post.category).exclude(pk=post.id)
      except Post.DoesNotExist:
            raise Http404("Post does not exist!!")  
     
      # logger = logging.getLogger('TestLogger')
      # logger.debug(f"post variable is {post}")
      return render(request,'detail.html',{'post': post, 'related_posts': related_posts})
 

def old_url_redirect(request, post_id):
      return redirect('new_url')

def new_url(request):
      return HttpResponse("This is the new URL page.")

def contact_view(request):
    if request.method == 'POST':
      form = ContactForm(request.POST)
      name = request.POST.get('name')
      email = request.POST.get('email')
      message = request.POST.get('message')
       
      logger = logging.getLogger('TESTING')
      if form.is_valid():
          logger.debug(f'POST data is {form.cleaned_data['name']} {form.cleaned_data['email']} {form.cleaned_data['message']}')
          success_message = "Your email has been sent successfully!😎"
          return render(request, 'contact.html', {'form': form, 'success_message':success_message})
      else:
            logger.debug(f'Form validation failure')
      return render(request, 'contact.html', {'form': form, 'name': name, 'email': email, 'message': message})                  
    return render(request, 'contact.html')

      


