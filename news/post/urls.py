from django.urls import path,include
from .views import index,post,category
appname = 'post'
urlpatterns = [
    path('',index,name='index'),
    path('category/',category,name='category'),
    path('post/<pk>',post,name='post'),


]