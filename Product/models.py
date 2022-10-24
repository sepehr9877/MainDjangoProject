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
class Product(models.Model):
    Rate = [
        ('High', 'High'),
        ('Low', 'Low'),
        ('Affordable', 'Affordable')
    ]
    SizeRate=[
            ('XS', 'XS'),
            ('SM', 'SM'),
            ('LG', 'LG'),
            ('XXL', 'XXL')
    ]
    title=models.CharField(max_length=150)
    image=models.ImageField(upload_to=UploadImage,null=True)
    description=models.CharField(max_length=150)
    price=models.IntegerField(default=0,null=True,blank=True)
    rate=models.CharField(choices=Rate,max_length=50,null=True,blank=True)
    size=models.CharField(choices=SizeRate,blank=True,null=True,max_length=50)

    def __str__(self):
        return self.title
class ProductDetail(models.Model):
    Pro_Detail=models.ForeignKey(Product,on_delete=models.CASCADE)
    Pro_Cat=models.ForeignKey(Category,on_delete=models.CASCADE)
    def __str__(self):
        return  self.Pro_Detail.title +self.Pro_Cat.ParentCategory
