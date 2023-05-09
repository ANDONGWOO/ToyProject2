from django.db import models
from django.contrib.auth.models import AbstractUser
# # Create your models here.

class User(AbstractUser):
    is_running = models.BooleanField(default=False)#공부 여부
    start=models.IntegerField(default=0)
    end=models.IntegerField(default=0)