#from iCoder.blog.models import Post
from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Post

# Create your views here.

def blogHome(request):
    allposts=Post.objects.all()
    context = {'allposts':allposts}
    return render(request,'blog/blogHome.html',context)


def blogPost(request,slug):
    post=Post.objects.filter(slug=slug).first()
    print(post)
    context = {'post':post}
    return render(request,'blog/blogPost.html',context)

