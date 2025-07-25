from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login, authenticate, logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from App_Users.forms import SignUpForm, UserProfileChange, ProfilePic, UserProfile

# Create your views here.
def sign_up(request):
    form = SignUpForm()
    registered = False
    if request.method == 'POST':
        form = SignUpForm(data=request.POST)
        if form.is_valid():
            form.save()
            registered = True

    dict = {'form':form, 'registered':registered}
    return render(request, 'App_Users/signup.html', context=dict )


def login_page(request):
    form = AuthenticationForm
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
    return render(request, 'App_Users/login.html', context={'form':form} )


@login_required
def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('App_Users:signin'))


@login_required
def profile(request):
    return render(request, 'App_Users/profile.html', context={})



@login_required
def user_change(request):
    current_users = request.user
    form = UserProfileChange(instance=current_users)
    if request.method =="POST":
        form = UserProfileChange(request.POST, instance=current_users)
        if form.is_valid():
            form.save()
            form = UserProfileChange(instance=current_users)
    return render(request, 'App_Users/change_profile.html', context={'form':form})



@login_required
def password_change(request):
    current_user = request.user
    change = False
    form = PasswordChangeForm(current_user)
    if request.method == "POST":
        form = PasswordChangeForm(current_user, data=request.POST)
        if form.is_valid():
            form.save()
            change = True
    return render(request, 'App_Users/pass_change.html', context={'form':form})



@login_required
def add_profile_pic(request):

    form = ProfilePic()
    if request.method == 'POST':
        form = ProfilePic(request.POST, request.FILES)
        if form.is_valid():
            user_obj = form.save(commit=False)
            user_obj.user = request.user
            user_obj.save()
        return HttpResponseRedirect(reverse('App_Users:profile'))

    return render(request, 'App_Users/add_pro_pic.html', context={'form':form})

@login_required
def change_pro_pic(request):
    form = ProfilePic(instance=request.user.user_profile)
    if request.method == 'POST':
        form = ProfilePic(request.POST, request.FILES, instance=request.user.user_profile)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('App_Users:profile'))
    return render(request, 'App_Users/add_pro_pic.html', context={'form':form})