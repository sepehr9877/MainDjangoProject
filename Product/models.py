import os.path
from django.db import models
from django.db.models import Q
from django.urls import reverse
from SizeColor.models import Sizes,Colors
from Categories.models import Category
# Create your models here
def Getfilename(filepath):
    base_name=os.path.basename(filepath)
    name,ex=base_name.split(base_name)
    return name,ex
def UploadImage(instance,filepath):
    name,ex=Getfilename(filepath)
    filename=f"{instance.id}---{instance.title}{ex}"
    return f"Product/{filename}"
class ProductMange(models.Manager):
    def get_valueslist(self,Queryset_dictionary):
        itemlist=[]
        for dictionary in Queryset_dictionary:
            for key in dictionary:
                itemlist.append(dictionary.get(key))
        itemlist=set(itemlist)
        return itemlist
class Product(models.Model):

    Rate = [
        ('High', 'High'),
        ('Low', 'Low'),
        ('Affordable', 'Affordable')
    ]
    title=models.CharField(max_length=150)
    image=models.ImageField(upload_to='Photos/Product/',null=True)
    description=models.CharField(max_length=150)
    price=models.IntegerField(default=0,null=True,blank=True)
    rate=models.CharField(choices=Rate,max_length=50,null=True,blank=True)
    brand=models.CharField(max_length=50,default="Tommy")
    objects=ProductMange()



    def __str__(self):
        return self.title
class ProductDetail_Manger(models.Manager):
    def GetallProducts(self):
        products=ProductDetail.objects.all().values_list('Pro_Detail_id')
        selected_products=[]
        for item in set(products):
            selected_products.append(ProductDetail.objects.filter(Pro_Detail_id=item[0]).first())
        return selected_products
    def Searhcitem(self,name):
        serachitem=ProductDetail.objects.filter(Pro_Detail__title__contains=name).values_list('Pro_Detail_id')
        search_result=[]
        print(serachitem)
        for item in set(serachitem):
            search_result.append(ProductDetail.objects.filter(Pro_Detail_id=item[0]).first())
        print("search")
        print(search_result)
        return search_result
    def convert_value_to_list(self,QuerySetDictionary):
        list_vlaue=[]
        for dictionary in QuerySetDictionary:
            for key in dictionary:
                list_vlaue.append(dictionary.get(key))
        return list_vlaue
class ProductDetail(models.Model):
    Pro_Detail=models.ForeignKey(Product,on_delete=models.CASCADE)
    Pro_Cat=models.ForeignKey(Category,on_delete=models.CASCADE)
    Pro_size=models.ForeignKey(Sizes,on_delete=models.CASCADE,null=True,blank=True)
    Pro_color=models.ForeignKey(Colors,on_delete=models.CASCADE,null=True,blank=True)
    objects=ProductDetail_Manger()

    def pass_value_to_url(self):
        return reverse('ProductDetailView',args=[self.id])
    def __str__(self):
        return  self.Pro_Detail.title +self.Pro_Cat.ParentCategory
