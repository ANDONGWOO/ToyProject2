from django.contrib.auth.forms import UserCreationForm
from .models import *
from django.contrib.auth import get_user_model
from django import forms

class test(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = [
            "end",
        ]