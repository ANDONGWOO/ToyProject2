from django.shortcuts import render

# Create your views here.


def home(request):#로그인 화면
    return render(request, "stopwatch/home.html")
def index(request):
    return render(request, "stopwatch/index.html")