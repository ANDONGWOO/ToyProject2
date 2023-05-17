from django import forms
from .models import *
from django.contrib.auth import get_user_model

class testForm(forms.ModelForm):
    class Meta:
        model = test
        fields = [
            "end_time",
        ]