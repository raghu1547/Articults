from django.db import models
from django.urls import reverse
from django.conf import settings
#import misaka
from groups.models import Group
# Create your models here.
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth import get_user_model
User = get_user_model()

class Post(models.Model):
    user = models.ForeignKey(User,related_name='posts',on_delete=models.CASCADE,unique=False)
    created_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=30,unique=False)
    content = RichTextUploadingField()
    publish = models.BooleanField(default=True)
    group = models.ForeignKey(Group,related_name='posts',null=True,blank=True,on_delete=models.CASCADE)


    def __str__(self):
        return self.title

    def save(self,*args,**kwargs):
     #   self.message_html= self.message
        super().save(*args,**kwargs)

    def get_absolute_url(self):
        return reverse('posts:all')

    class Meta:
        ordering = ['-created_at']
        unique_together = ['user','content','title']