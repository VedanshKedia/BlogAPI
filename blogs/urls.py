from django.urls import path

from . import views

urlpatterns = [
    path('profile/', views.profile_form, name='profile_form'),
    path('', views.blog_form, name='blog_form'),
    path('blogs/', views.blogs, name='blogs'),
]
