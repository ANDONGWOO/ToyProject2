from django.shortcuts import render

# Create your views here.
def index(request):#시작
    return render(request, "accounts/index.html")