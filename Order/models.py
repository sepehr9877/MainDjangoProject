from django.db import models
from Account.models import Account,User
from Product.models import ProductDetail
# Create your models here.
class Order(models.Model):
    UserOder=models.ForeignKey(Account,on_delete=models.CASCADE)
    PriceOrder=models.IntegerField(null=True,blank=True)
    OrderDate=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.UserOder.user.username
class OrderDetail(models.Model):
    orderdetail=models.ForeignKey(Order,on_delete=models.CASCADE)
    productorder=models.ForeignKey(ProductDetail,on_delete=models.CASCADE)
    order_count=models.IntegerField(max_length=5,null=True,blank=True)
    purchase=models.BooleanField(default=False)


    def __str__(self):
        return self.orderdetail.UserOder.user.username +"____"+self.productorder.Pro_Detail.title+"_____"+self.productorder.Pro_color.Color_Rate
