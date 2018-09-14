from django.urls import path,include
from .views import index,post,indian_news,entertainment
appname = 'post'
urlpatterns = [
    path('',index,name='index'),
    path('indian_news/',indian_news,name='indian_news'),
    path('entertainment/',entertainment,name='entertainment'),
    path('post/<pk>',post,name='post'),


]