from django.db import models
from Account.models import Account
# Create your models here.
class Comments(models.Model):
    User_Comment=models.ForeignKey(Account,on_delete=models.CASCADE)
    Description=models.CharField(max_length=150)
    DataCreated=models.DateTimeField(auto_now_add=True)