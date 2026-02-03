from django.urls import path
from . import views

app_name = 'blog'


urlpatterns = [
      path("", views.index, name='index'),
      
      path("post/<slug:slug>", views.detail, name='detail'),
      
      #path('new_url', views.new_url, name='new_url'),

      path('contact', views.contact_view, name='contact'),
      path('about', views.about_view, name='about'),
]