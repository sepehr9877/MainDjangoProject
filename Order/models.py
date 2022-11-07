from django.db import models
from Account.models import Account,User
from Product.models import ProductDetail
# Create your models here.
class Order(models.Model):
    UserOder=models.ForeignKey(Account,on_delete=models.CASCADE)
    PriceOrder=models.IntegerField(null=True,blank=True)
    OrderDate=models.DateTimeField(auto_now_add=True)
    transaction=models.BooleanField(default=False)
    def __str__(self):
        return self.UserOder.user.username +"___"+str(self.OrderDate.date())+"__"+str(self.transaction)
class OrderDetail(models.Model):
    orderdetail=models.ForeignKey(Order,on_delete=models.CASCADE)
    productorder=models.ForeignKey(ProductDetail,on_delete=models.CASCADE)
    order_count=models.IntegerField(default=1)
    purchase=models.BooleanField(default=False)
    received=models.BooleanField(default=False)
    @property
    def totalpriceorder(self):
        return self.productorder.Pro_Detail.price*self.order_count


    def __str__(self):
        return self.orderdetail.UserOder.user.username +"____"+self.productorder.Pro_Detail.title+"_____"+self.productorder.Pro_color.Color_Rate
class ShippingDetail(models.Model):
    ShipOrder=models.ForeignKey(Order,on_delete=models.CASCADE)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    Country = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    street = models.CharField(max_length=50)
    building = models.CharField(max_length=50)
    house = models.CharField(max_length=50)
    postalcode = models.CharField(max_length=50)
    zip = models.CharField(max_length=50)

    def __str__(self):
        return self.ShipOrder.UserOder.user.username
class CardSpecification(models.Model):
    CardOrder=models.ForeignKey(Order,on_delete=models.CASCADE)
    CardNumber=models.CharField(max_length=50)
    CsvCard=models.CharField(max_length=10)
    CardYear=models.IntegerField()
    CardMonth=models.IntegerField()
    def __str__(self):
        return self.CardOrder.UserOder.user.username +"____"+ str(self.CardOrder.OrderDate.date())