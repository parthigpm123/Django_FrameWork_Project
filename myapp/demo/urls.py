from django.urls import path
from . import views 

urlpatterns = [
      path('gm/', views.gm, name='gm'),
      path('ga/', views.ga, name='ga'),
      path('ge/', views.ge, name='ge'),
]
