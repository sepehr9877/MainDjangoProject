from django.db.models import Sum
from django.http import JsonResponse
from django.shortcuts import render, redirect
from Product.models import ProductDetail
# Create your views here.
from .models import OrderDetail,Order,ShippingDetail
from django.views.generic import CreateView, ListView, DetailView
from Account.models import Account,User
from .forms import ShippingForm

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
        print("Data")
        print(data)
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
        print("self.Orderdetail")
        print(self.Orderdetail)
        CheckOrder=OrderDetail.objects.filter(id=self.Orderdetail.id)
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
        print("selected_account")
        print(selected_account)
        totalprice= OrderDetail.objects.filter(orderdetail__UserOder_id=selected_account.id, purchase=False).aggregate(total_sum=Sum('productorder__Pro_Detail__price'))
        context['totalsum']=totalprice['total_sum']
        context['total']=context['totalsum']-10
        return context

def Removeitem(request,**kwargs):
    productdetailid=kwargs['productdetailid']
    userid=request.user.id
    selected_account=Account.objects.filter(user_id=userid).first()
    selected_order=Order.objects.filter(UserOder_id=selected_account.id).first()
    selected_orderdetail=OrderDetail.objects.filter(orderdetail_id=selected_order.id,productorder_id=productdetailid).delete()
    return redirect("/CartPage")


class CheckCard(DetailView):
    template_name = 'Order/CheckCard.html'

    def get_object(self, queryset=None):
        userid = self.request.user.id
        account_sl = Account.objects.filter(user_id=userid).first()
        order_sl = Order.objects.filter(UserOder_id=account_sl.id).first()
        order_detail = OrderDetail.objects.filter(orderdetail_id=order_sl.id, purchase=False).all()
        print(order_detail)
        queryset=order_detail
        return queryset
    def post(self, request, *args, **kwargs):
        deliveryform=ShippingForm(data=self.request.POST or None)
        print("Post")
        if(deliveryform.is_valid()):
            firstname=deliveryform.cleaned_data['firstname']
            print(firstname)
            lastname=deliveryform.cleaned_data['lastname']
            email=deliveryform.cleaned_data['email']
            phone=deliveryform.cleaned_data['phone']
            zip=deliveryform.cleaned_data['zip']
            house=deliveryform.cleaned_data['house']
            building=deliveryform.cleaned_data['building']
            street=deliveryform.cleaned_data['street']
            state=deliveryform.cleaned_data['state']
            postalcode=deliveryform.cleaned_data['postalcode']
            orderuser=Order.objects.filter(UserOder_id=self.request.user.id).first()
            createshipping=ShippingDetail.objects.create(ShipOrder_id=orderuser.id,firstname=firstname,lastname=lastname,
                                                         email=email,phone=phone,
                                                         zip=zip,house=house,
                                                         building=building,street=street,
                                                         state=state,postalcode=postalcode)
            return redirect("/")


    def get_context_data(self,*args,**kwargs):
        context=super(CheckCard, self).get_context_data(*args,**kwargs)
        userid=self.request.user.id
        account=Account.objects.filter(user_id=userid).first()
        sum_order=OrderDetail.objects.filter(orderdetail__UserOder_id=account.id,purchase=False).aggregate(total_sum=Sum('productorder__Pro_Detail__price'))
        context['totalsum']=sum_order['total_sum']
        context['finalprice']=context['totalsum']-10
        initial_data={
            "firstname":self.request.user.username,
            "lastname":self.request.user.last_name,
            "email":self.request.user.email,

        }
        addressform = ShippingForm(initial=initial_data)
        context['address']=addressform
        return context




