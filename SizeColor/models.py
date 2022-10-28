from django.db import models

# Create your models here.
class Sizes(models.Model):
    SizeRate = [
        ('S', 'S'),
        ('M', 'M'),
        ('XS', 'XS'),
        ('SM', 'SM'),
        ('LG', 'LG'),
        ('XXL', 'XXL')
    ]
    SizeRate=models.CharField(choices=SizeRate,max_length=50)
    def __str__(self):
        return self.SizeRate

class Colors(models.Model):
    ColorRate=[
        ('black', 'black'),
        ('grey', 'grey'),
        ('red', 'red'),
        ('blue', 'blue'),
        ('brown', 'brown'),
        ('white', 'white')
    ]
    SizeRate=models.CharField(choices=ColorRate,max_length=50)
    def __str__(self):
        return self.SizeRate