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




from django.core.files.images import get_image_dimensions

class UserProfileInfoForm(forms.ModelForm):
    profile_pic = forms.FileField(widget=ClearableFileInput)
    class Meta():
        model = Profile
        fields = ('prof_url','profile_pic')
    
    
    def clean_profile_pic(self):
        profile_pic = self.cleaned_data['profile_pic']

        try:
            w, h = get_image_dimensions(profile_pic)

            # #validate dimensions
            # max_width = max_height = 100000
            # if w > max_width or h > max_height:
            #     raise forms.ValidationError(
            #         u'Please use an image that is '
            #          '%s x %s pixels or smaller.' % (max_width, max_height))

            #validate content type
            main, sub = profile_pic.content_type.split('/')
            if not (main == 'image' and sub in ['jpeg', 'pjpeg', 'gif', 'png']):
                raise forms.ValidationError(u'Please use a JPEG, '
                    'GIF or PNG image.')

            #validate file size
            if len(profile_pic) > (2 * 1024 * 1024):
                raise forms.ValidationError(
                    u'Photo file size may not exceed 2mb.')

        except AttributeError:
            """
            Handles case when we are updating the user profile
            and do not supply a new avatar
            """
            pass

        return profile_pic



class UserProfileInfoForm1(forms.ModelForm):
   
    class Meta():
        model = Profile
        fields = ('prof_url','profile_pic')
