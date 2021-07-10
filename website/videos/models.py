from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class Video(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    video = models.FileField(upload_to='videos')
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    views = models.IntegerField(default=0)
    def __str__(self):
        return self.title
    class Meta:
        ordering = ["-created"]


class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='profile',on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    username = models.CharField(max_length=30, default = "Anonymous", unique=True)
    email = models.EmailField(max_length=255)
    picture = models.ImageField(upload_to='images', default = "media/images/defaultprofilepicture.png",max_length=1000)
    contact_no = models.CharField(max_length=11)
    videos = models.ManyToManyField(Video,blank=True)
    forget_password_token = models.CharField(max_length=100)


    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']
    User._meta.get_field('email')._unique = True


    def __str__(self):
        return self.username

    class Meta:
        ordering = ["-username",]


