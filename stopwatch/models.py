from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
# Create your models here.


class test(models.Model):
    end_time=models.IntegerField()
    user=models.ForeignKey(get_user_model(), on_delete=models.CASCADE)#유저 id
    time=models.DateTimeField(auto_now_add=True)#저장 시간