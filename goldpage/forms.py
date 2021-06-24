from django.forms import fields

from django import forms
from .models import User
class Userform(forms.ModelForm):
    class Meta:
        model=User
        fields={'usrmail','usrpass','usrprofile','usrphoto'}
        labels={'usrphoto':'','usrpass':'Password','usrmail':'Email','usrprofile':'Profile pic'}
    

