from django.db import models
from Account.models import UserProfile
from Product.models import ProductDetail
# Create your models here.
class Order(models.Model):
    UserOder=models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    PriceOrder=models.IntegerField(null=True,blank=True)
    OrderDate=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.UserOder.username
class OrderDetail(models.Model):
    orderdetail=models.ForeignKey(Order,on_delete=models.CASCADE)
    productorder=models.ForeignKey(ProductDetail,on_delete=models.CASCADE)


    def __str__(self):
        return self.orderdetail.UserOder.username +"____"+self.productorder.Pro_Detail.title+"_____"+self.productorder.Pro_color.Color_Rate
