from django.urls import path
from .views import *

urlpatterns = [
    path('home/',homepage, name='home'),
    path('home/<int:pk>/',category, name='category'),
    path('slug/<slug:slug>/',single_blog, name='single_blog'),
    path('search/', search, name='search'),
]