from django.shortcuts import render

# Create your views here.


def home(request):#로그인 화면
    return render(request, "stopwatch/home.html")
def index(request):#시작
    return render(request, "stopwatch/index.html")
def stop(request):#정지
    return render(request, "stopwatch/stop.html")