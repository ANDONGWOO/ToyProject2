from django.shortcuts import render,redirect
from .forms import testForm
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def index(request):#경과시간
    print(0)
    user = request.user
    user.is_running=0#기본 값으로 변경
    user.save()
    test_1=get_user_model().objects.filter(is_running=1)
    test_0=get_user_model().objects.filter(is_running=0)
    context={
        "test_1":test_1,
        "test_0":test_0,
    }
    return render(request, "stopwatch/index.html",context)

@login_required
def stop(request):
    print(1)
    user = request.user
    user.is_running=1#기본 값으로 변경
    user.save()
    test_1=get_user_model().objects.filter(is_running=1)
    test_0=get_user_model().objects.filter(is_running=0)
    if request.method =="POST":
        form=testForm(request.POST)
        if form.is_valid():
            test=form.save(commit=False)
            test.user = request.user#유저정보
            test.save()#유저정보       
        return redirect('stopwatch:index')
    else:
        form = testForm()
    context={
        "form": form,
        "test_1":test_1,
        "test_0":test_0,
    }
    return render(request, "stopwatch/stop.html",context)


