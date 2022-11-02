from django.db.models import Sum
from django.http import JsonResponse
from django.shortcuts import render
from Product.models import ProductDetail
# Create your views here.
from .models import OrderDetail,Order
from django.views.generic import CreateView, ListView, DetailView
from Account.models import Account,User

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
        selected_account=Account.objects.filter(user_id=userid).first()
        user_order=Order.objects.filter(UserOder_id=selected_account.id)
        print(user_order)
        if len(user_order)==0:
            user_order=Order.objects.create(UserOder_id=selected_account.id)

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

class CartPage(DetailView):
    template_name = 'Order/CartPage.html'
    def get_object(self, queryset=None):
        userid=self.request.user.id
        selected_account=Account.objects.filter(user_id=userid).first()
        queryset=OrderDetail.objects.filter(orderdetail__UserOder_id=selected_account.id,purchase=False)
        return queryset
    def get_context_data(self, *args,**kwargs):
        context=super(CartPage, self).get_context_data(*args,**kwargs)
        userid = self.request.user.id
        selected_account = Account.objects.filter(user_id=userid).first()
        context["totalsum"] = OrderDetail.objects.filter(orderdetail__UserOder_id=selected_account.id, purchase=False).annotate(total_sum=Sum('productorder__Pro_Detail__price')).values_list('total_sum')[0][0]
        context['total']=context['totalsum']-10
        return context





