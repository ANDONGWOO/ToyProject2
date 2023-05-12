from django.shortcuts import render,redirect
from .forms import CustomUserCreationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
# Create your views here.

def home(request):#로그인 화면
    return render(request, "accounts/home.html")

def create(request):#회원가입
    if request.method =="POST":
        form =CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('stopwatch:index')
    else:
        form = CustomUserCreationForm()
    context={
        "form": form
    }
    return render(request, "accounts/create.html",context)

def login(request):
    if request.method =="POST":
        form_login = AuthenticationForm(request, data=request.POST)
        if form_login.is_valid():
            auth_login(request, form_login.get_user())
            return redirect(request.GET.get("next") or "stopwatch:index")
    else:
        form_login = AuthenticationForm()
    context={
        "form": form_login
    }
    return render(request, "accounts/home.html", context)

@login_required
def logout(request): 
    auth_logout(request)
    return redirect('home')