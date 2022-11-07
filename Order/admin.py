from django.contrib import admin
from .models import CardSpecification,Order,OrderDetail,ShippingDetail
# Register your models here.
admin.site.register(Order)
admin.site.register(OrderDetail)
admin.site.register(ShippingDetail)
admin.site.register(CardSpecification)
