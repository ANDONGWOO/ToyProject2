from django.urls import path
from . import views

app_name="stopwatch"

urlpatterns = [
    path("",views.index, name="index"),#시작
    path("stop",views.stop, name="stop"),
    
]
