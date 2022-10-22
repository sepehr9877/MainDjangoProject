from django.contrib.auth.base_user import BaseUserManager,AbstractBaseUser
from django.db import models
# Create your models here.
class UserManger(BaseUserManager):
    def create_user(self,firstname,lastname,username,email,password=None,gender=None,city=None,country=None):
        if not email:
            raise ValueError("Email needs to be completed")
        if not username:
            raise ValueError("Username needs to be completed")
        if not password:
            raise ValueError("Password needs to be completed")
        user=self.model(
            email=self.normalize_email(email),
            username=username,
            firstname=firstname,
            lastname=lastname,
            gender=gender,
            city=city,
            country=country
        )
        user.set_password(password)
        user.save(using=self.db)
        return user
    def create_superuser(self,firstname,username,lastname,email,password=None):
        user=self.create_user(
            email=self.normalize_email(email),
            firstname=firstname,
            lastname=lastname,
            username=username
        )
        user.set_password(password)
        user.is_superadmin=True
        user.is_staff=True
        user.is_active=True
        user.save(using=self.db)
        return user

class Account(AbstractBaseUser):
    email=models.CharField(max_length=150,null=True)
    firstname=models.CharField(max_length=150)
    username=models.CharField(max_length=150,unique=True)
    lastname=models.CharField(max_length=150)
    city=models.CharField(max_length=50)
    country=models.CharField(max_length=50)
    gender=models.CharField(default="Male",max_length=10)
    is_superadmin=models.BooleanField(default=False)
    is_active =models.BooleanField(default=False)
    is_staff=models.BooleanField(default=False)
    image=models.ImageField(upload_to='user',null=True)
    USERNAME_FIELD=['username']
    Object=UserManger()

