import os.path

from django.contrib.auth.base_user import BaseUserManager,AbstractBaseUser
from django.db import models
# Create your models here.
from django.contrib.auth.models import User
class Account(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    image=models.ImageField(upload_to='user',null=True)
    city = models.CharField(max_length=50,null=True,blank=True)
    country = models.CharField(max_length=50,null=True,blank=True)
    gender = models.CharField(default="Male", max_length=10)

    def __str__(self):
        return self.user.username




