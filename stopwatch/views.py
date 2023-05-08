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
    return render(request, "stopwatch/stop.html")