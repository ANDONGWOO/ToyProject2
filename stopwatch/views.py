from django.shortcuts import render,redirect
import time
# Create your views here.


def home(request):#로그인 화면
    return render(request, "stopwatch/home.html")

def index(request):#경과시간
    # if not is_running:
    #     is_running=True#DB추가 기본 False
    #     start_time =time.time()
    #     print(start_time)
    return render(request, "stopwatch/index.html")

def stop(request):
    # is_running = False#DB추가
    print(1)
    print(request.POST)
    if request.method =="POST":
        print(1)
        print(request.POST)
        form= form(request.POST)
        print(request.POST)
        print(1)
        if form.is_valid():
            print(request.POST)
    return render(request, "stopwatch/stop.html")