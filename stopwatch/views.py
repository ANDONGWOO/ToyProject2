from django.shortcuts import render,redirect
from .forms import testForm
from django.contrib.auth import get_user_model
from .models import test
from django.contrib.auth.decorators import login_required
from django.utils import timezone
import datetime
# Create your views here.

@login_required
def index(request):#경과시간
    user = request.user
    user.is_running=0#기본 값으로 변경
    user.save()
    #오늘 누적
    today_start = timezone.now().replace(hour=0, minute=0, second=0, microsecond=0)
    my_objects = test.objects.all().filter(time=today_start, user=request.user)
    total_sum = str(datetime.timedelta(seconds=sum(i.end_time for i in my_objects)))#오늘 누적 시간형식
    #오늘 누적
    is_running_1=get_user_model().objects.filter(is_running=1)
    is_running_0=get_user_model().objects.filter(is_running=0)
    context={
        "is_running_1":is_running_1,
        "is_running_0":is_running_0,
        "my_objects":my_objects,
        "total_sum":total_sum,
    }
    return render(request, "stopwatch/index.html",context)

@login_required
def stop(request):
    user = request.user
    user.is_running=1#기본 값으로 변경
    user.save()
    is_running_1=get_user_model().objects.filter(is_running=1)
    is_running_0=get_user_model().objects.filter(is_running=0)
    if request.method =="POST":
        form=testForm(request.POST)
        if form.is_valid():
            form=form.save(commit=False)
            form.user = request.user#유저정보
            form.save()#유저정보       
        return redirect('stopwatch:index')
    else:
        form = testForm()
    context={
        "form": form,
        "is_running_1":is_running_1,
        "is_running_0":is_running_0,
    }
    return render(request, "stopwatch/stop.html",context)


