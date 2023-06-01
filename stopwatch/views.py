from django.shortcuts import render,redirect
from .forms import testForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def index(request):#경과시간
    return render(request, "stopwatch/index.html")

@login_required
def stop(request):
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
        "form": form
    }
    return render(request, "stopwatch/stop.html",context)


