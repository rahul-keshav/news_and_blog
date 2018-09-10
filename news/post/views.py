from django.shortcuts import render,redirect,reverse,get_object_or_404
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView,View
# Create your views here.
from .models import Post
from django.utils.timezone import now


def index(request):
    return render(request, 'post/index.html',)

def post(request,pk):
    post = get_object_or_404(Post,pk=pk)
    return render(request, 'post/single_center.html',{'now':now(),'post':post})




# def post_2(request):
#     return render(request, 'post/single_center.html',)





