from django import forms
from .models import *


class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','content','group')

    def __init__(self,*args,**kwargs):
        super(CreatePostForm,self).__init__(*args,**kwargs)
        self.fields['content'].attrs={
            'id': 'myTextarea',
            'name': 'myCustomName',
            'placeholder': 'myCustomPlaceholder'}


