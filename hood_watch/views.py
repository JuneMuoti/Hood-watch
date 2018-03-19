
from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from .models import Post,Neighbourhood,User,Business
from .forms import ProfileForm,PostForm,HoodForm
from django.contrib import messages
from django.db import transaction


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
def join_hood(self,request):

    hood=get_object_or_404(Neighbourhood)
    try:
        User.objects.create(self.request.user,hood=hood)
    except:
        messages.warning(self.request,"You are already a member!")
    else:
        messages.success(self.request,'You are now a member!')

    return redirect(request,'my_hood.html',{'hood':hood,'messages':messages})
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
def search_results(request):
    if 'business' in request.GET and request.GET["business"]:
        queryList = request.GET.get("business")
        searched_business = Business.search_by_hood(queryList)
        message = f"{queryList}"

        return render(request, 'search.html',{"message":message,"business": searched_business})

    else:
        message = "You haven't searched for any businesses"
        return render(request, 'search.html',{"message":message})
def user_profile(request):
    current_user = request.user
    user=User.objects.get(id=current_user.id)
    return render(request,'profile.html',{'user':user})

@transaction.atomic
def change_hood(request):
        current_user = request.user
        if request.method == 'POST':
            form = HoodForm(request.POST )
            if form.is_valid():
                hood=form.save(commit=False)
                hood.save()
                

                return redirect(user_profile)
        else:
            form = HoodForm( )
        return render(request, 'new_hood.html', {"form": form})


# Create your views here.
