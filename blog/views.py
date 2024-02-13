from django.shortcuts import redirect, render
from .models import Post

def home(request):   
    return redirect('sign_in')

#shall be removed in future
def index(request):
    context = {
        'posts': Post.objects.all(),
    }
    return render(request, 'blog/index.html', context)