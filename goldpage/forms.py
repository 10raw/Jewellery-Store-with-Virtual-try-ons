
from django.forms import fields

from django import forms
from .models import Details
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# class Useracc(UserCreationForm):
#     email=forms.CharField(max_length=60,blank=True)
#     usrphoto=forms.ImageField(upload_to="usrphotos/",blank=True)
#     usrprofile=forms.ImageField(upload_to="usrprofile/",blank=True)
#     class Meta:
#         model=User
#         fields={'username','email','password1','password2'}

class detailsform(forms.ModelForm):
    class Meta:
        model=Details
        fields=['usrph']

