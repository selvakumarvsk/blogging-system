from django.urls import path
from .views import *

urlpatterns = [
    path('',dashboard,name='dashboard'),

    # category
    path('category_view/', category_view, name='category_view'),
    path('category_add/', category_add, name='category_add'),
    path('category_edit/<int:pk>/', category_edit, name='category_edit'),
    path('category_delete/<int:pk>/',category_delete, name='category_delete'),

    # post
    path('post_view/', post_view, name='post_view'),
    path('post_add/', post_add, name='post_add'),
    path('post_edit/<int:pk>/',post_edit, name='post_edit'),
    path('post_delete/<int:pk>/',post_delete, name='post_delete'),

    # user
    path('user_view/', user_view, name='user_view'),
    path('user_add/', user_add, name='user_add'),
    path('user_edit/<int:pk>/', user_edit, name='user_edit'),
    path('user_delete/<int:pk>/', user_delete, name='user_delete'),
]