import os.path
from django.db import models

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
        return itemlist
class Product(models.Model):
    SizeRate = [
        ('S', 'S'),
        ('M', 'M'),
        ('XS', 'XS'),
        ('SM', 'SM'),
        ('LG', 'LG'),
        ('XXL', 'XXL')
    ]
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
    ProSize=models.CharField(choices=SizeRate,max_length=50,null=True)
    objects=ProductMange()



    def __str__(self):
        return self.title
class ProductDetail(models.Model):
    Pro_Detail=models.ForeignKey(Product,on_delete=models.CASCADE)
    Pro_Cat=models.ForeignKey(Category,on_delete=models.CASCADE)
    def __str__(self):
        return  self.Pro_Detail.title +self.Pro_Cat.ParentCategory
