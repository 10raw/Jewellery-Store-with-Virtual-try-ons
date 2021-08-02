from django import forms
from captcha.fields import ReCaptchaField
from django.forms import fields
from .models import Details

class payment(forms.ModelForm):
    captcha=ReCaptchaField()
    class Meta:
        model=Details
        fields=['usraddress','usrphoneno']

