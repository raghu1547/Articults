from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):

    user = models.OneToOneField(User,on_delete=models.CASCADE)

    prof_url = models.URLField(blank=True)

    profile_pic = models.ImageField(default='default.png',upload_to='profile_pics',blank=True,null=True)

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

        profile_pic = Image.open(self.profile_pic.path)

        if profile_pic.height > 300 or profile_pic.width > 300:
            output_size = (300, 300)
            profile_pic.thumbnail(output_size)
            profile_pic.save(self.profile_pic.path)

