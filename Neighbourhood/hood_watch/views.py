from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Post


@login_required(login_url='/accounts/login/')
def index(request):
    post=Post.get_post()
    return render(request,'index.html',{'post':post})

# Create your views here.
