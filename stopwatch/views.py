from django.shortcuts import render,redirect
import time
from .forms import testForm
from accounts.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.



@login_required
def index(request):#경과시간
    # if not is_running:
    #     is_running=True#DB추가 기본 False
    #     start_time =time.time()
    #     print(start_time)
    return render(request, "stopwatch/index.html")
@login_required
def stop(request):
    # is_running = False#DB추가
    if request.method =="POST":
        form=testForm(request.POST)
        ##3까지"
        if form.is_valid():
            form.save()
        return redirect('stopwatch:index')
    else:
        form = testForm()
    context={
        "form": form
    }
    return render(request, "stopwatch/stop.html",context)