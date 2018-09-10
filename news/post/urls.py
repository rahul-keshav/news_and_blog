from django.urls import path,include
from .views import index,post
appname = 'post'
urlpatterns = [
    path('',index,name='index'),
    path('post/<pk>',post,name='post'),


]