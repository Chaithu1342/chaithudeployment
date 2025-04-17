from django.db import models
from django.contrib.auth.models import User
class UserProfileInfo(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    portfolio_site=models.URLField(blank=True)
    profile_pic=models.ImageField(upload_to='profile_pics',blank=True)
    def __str__(self):
        return self.user.username
from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    theme = models.CharField(max_length=50, default='light')
    notifications = models.CharField(max_length=50, default='enabled')

    def __str__(self):
        return f"{self.user.username}'s Profile"
