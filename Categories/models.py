from django.db import models

# Create your models here.
class Category(models.Model):
    Choices=[
        ('Man','Man'),
        ('Women','Women'),
        ('Electronic','Electronic'),
        ('Tshirt', 'Tshirt'),
        ('Pants', 'Pants'),
        ('Accessories', 'Accessories'),
        ('Bags', 'Bags'),
        ('Shoes','Shoes'),
        ('Jacket','Jacket')
    ]

    ParentCategory=models.CharField(choices=Choices,max_length=50,null=True,blank=True)
    Parentitem=models.ForeignKey('self',blank=True,null=True,related_name='children',on_delete=models.CASCADE)

    def __str__(self):
        fullpath=[self.ParentCategory]
        parent=self.Parentitem
        while parent is not None:
            fullpath.append(parent.ParentCategory)
            parent=parent.Parentitem
        return '->'.join(fullpath[::-1])