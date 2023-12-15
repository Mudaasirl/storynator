from django.shortcuts import render
from django.http import HttpResponse
from .models import Post,User
from users.models import Profile

def home(request):
    context={
        'pass':'pass'
    }
    return render(request,'blog/home.html',context)
def index(request):
    context = {
        'posts': Post.objects.all(),
    }
    return render(request, 'blog/index.html', context)
def get_all_users(request):
    context = {
        'users' : User.objects.all()
    }
  
    return render(request, 'blog/users.html', context)
def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
def greet(request, name):
    return HttpResponse(f"Hello, {name.capitalize()}!")
