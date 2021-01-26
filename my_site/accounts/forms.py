from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from accounts.models import *
from django.forms.widgets import FileInput,ClearableFileInput
from django.core import validators

class UserUpdateForm(forms.ModelForm):
    #email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username']


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username','email','password')

    def clean(self):
        cleaned_data = super().clean()
        p1 = cleaned_data.get("password")
        p2 = cleaned_data.get("confirm_password")

        if p1==p2:
            pass
        else:
            raise validators.ValidationError("Please Make Sure Your PassWords Match")




class UserProfileInfoForm(forms.ModelForm):
    profile_pic = forms.FileField(widget=ClearableFileInput)
    class Meta():
        model = Profile
        fields = ('prof_url','profile_pic')

class UserProfileInfoForm1(forms.ModelForm):
   
    class Meta():
        model = Profile
        fields = ('prof_url','profile_pic')
