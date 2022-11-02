from django.contrib import admin
from .models import Order,OrderDetail,ShippingDetail
# Register your models here.
admin.site.register(Order)
admin.site.register(OrderDetail)
admin.site.register(ShippingDetail)
