from django.urls  import path
from . import views
from django.conf import settings

urlspatterns =[
    path('', views.home name='home'),
    path('about/', views.home name='about'),
    path('menu/', views.home name='menu'),
    path('', views.home name='home'),
]