from django.http import JsonResponse
from django.shortcuts import render
from Product.models import ProductDetail
# Create your views here.
from .models import OrderDetail,Order
from django.views.generic import CreateView

def Creating(request):
    print(request.GET.get('selected_color'))
class CreatingOrder(CreateView):
    Orderdetail=None
    def get(self, request, *args, **kwargs):
        color=self.request.GET.get("color_value")
        size=self.request.GET.get("size_value")
        productid=self.request.GET.get("productid")
        print(productid,size,color)
        Order_User=self.create_order()
        Selected_Prodcut=self.check_productdetail(productid=productid,color=color,size=size)
        self.CreateOrderDetail(Product_Detail=Selected_Prodcut,OrderSpec=Order_User)
        created=self.CheckOrderDetail()
        data={
            "isCreated":created
        }
        return JsonResponse(data,safe=False)
    def create_order(self):
        userid=self.request.user.id
        user_order=Order.objects.filter(UserOder_id=3)
        print(user_order)
        if len(user_order)==0:
            user_order=Order.objects.create(UserOder_id=3)

        return user_order
    def check_productdetail(self,productid,color,size):
        selected_product=ProductDetail.objects.filter(Pro_Detail_id=productid,
                                                   Pro_color__Color_Rate=color,
                                                   Pro_size__SizeRate=size)
        return selected_product
    def CreateOrderDetail(self,Product_Detail,OrderSpec):
        print(Product_Detail,OrderSpec)
        OrderDetailEl=OrderDetail.objects.filter(orderdetail__in=OrderSpec,productorder__in=Product_Detail)
        if len(OrderDetailEl)==0:
            OrderDetailEl=OrderDetail.objects.create(orderdetail=OrderSpec[0], productorder=Product_Detail[0])
        self.Orderdetail = OrderDetailEl
        return OrderDetailEl
    def CheckOrderDetail(self):
        CheckOrder=OrderDetail.objects.filter(id=self.Orderdetail[0].id)
        if len(CheckOrder)==0:
            return False
        else:
            return True


