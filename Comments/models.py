from django.db import models
from Account.models import Account,User
from Product.models import ProductDetail
# Create your models here.
class Comments(models.Model):
    User_Comment=models.ForeignKey(Account,on_delete=models.CASCADE)
    Description=models.CharField(max_length=150)

    def __str__(self):
        return self.User_Comment.user.username
class CommentManger(models.Manager):
    def GetAllComments(self,productdetailid):
        return self.filter(ItemProduct_id=productdetailid).all()
class Product_Comment(models.Model):
    ItemComment=models.ForeignKey(Comments,on_delete=models.CASCADE)
    ItemProduct=models.ForeignKey(ProductDetail,on_delete=models.CASCADE)
    DataCreated=models.DateTimeField(auto_now_add=True)
    objects=CommentManger()

    def __str__(self):
        return self.ItemComment.User_Comment.user.username