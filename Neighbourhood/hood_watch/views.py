
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Post,Neighbourhood
from .forms import ProfileForm,PostForm


@login_required(login_url='/accounts/login/')
def post(request):
    post=Post.get_post()
    return render(request,'posts.html',{'post':post})
def index(request):

    return render(request,'landing.html')


@login_required(login_url='/accounts/login/')
def Profile(request):

    current_user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)

            profile.save()
    else:
        form = ProfileForm()
    return render(request, 'new_profile.html', {"form": form})
def my_hood(request):
    hood=Neighbourhood.get_hood()
    return render(request,'my_hood.html',{'hood':hood})
def join_hood(request):
    return redirect(request,'my_hood.html')
def leave_hood(request):
    return redirect(request,'my_hood.html')
@login_required(login_url='/accounts/login/')
def new_post(request):

    current_user = request.user
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)

            post.save()
    else:
        form = PostForm()
    return render(request, 'new_post.html', {"form": form})

# Create your views here.
