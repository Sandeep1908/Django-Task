from django.db import models
from django.contrib.auth.models import User

class userdata(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    token=models.CharField(max_length=1000,default='')
    Address=models.CharField(max_length=300,default='')
    
    def __str__(self):
        return self.user.username

