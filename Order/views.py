from django.db.models import Sum
from django.http import JsonResponse
from django.shortcuts import render, redirect
from Product.models import ProductDetail
# Create your views here.
from .models import OrderDetail,Order,ShippingDetail,CardSpecification
from django.views.generic import CreateView, ListView, DetailView
from Account.models import Account,User
from .forms import ShippingForm,CreditCardForm
import random
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
        user_order=Order.objects.filter(UserOder_id=selected_account.id,transaction=False)
        print(user_order)
        if len(user_order)==0:
            OrdreNumber = random.sample(range(100000, 10000000))
            createuser=Order.objects.create(UserOder_id=selected_account.id,OrderNumber=OrdreNumber)
        user_order = Order.objects.filter(UserOder_id=selected_account.id, transaction=False)
        return user_order
    def check_productdetail(self,productid,color,size):
        selected_product=ProductDetail.objects.filter(Pro_Detail_id=productid,
                                                   Pro_color__Color_Rate=color,
                                                   Pro_size__SizeRate=size,
                                                      )
        return selected_product
    def CreateOrderDetail(self,Product_Detail,OrderSpec):
        OrderDetailEl=OrderDetail.objects.filter(orderdetail=OrderSpec[0],productorder=Product_Detail[0])
        if len(OrderDetailEl)==0:
            OrderDetailEl=OrderDetail.objects.create(orderdetail=OrderSpec[0], productorder=Product_Detail[0])
        self.Orderdetail = OrderDetailEl
        return OrderDetailEl
    def CheckOrderDetail(self):
        CheckOrder=OrderDetail.objects.filter(id=self.Orderdetail.id)
        if len(CheckOrder)==0:
            return False
        else:
            return True

class CartPage(DetailView):
    template_name = 'Order/CartPage.html'
    def dispatch(self, request, *args, **kwargs):
        userid=self.request.user.id
        if userid is None:
            return redirect("/")
        else:
            return self.get(request)
    def get_object(self, queryset=None):
        userid=self.request.user.id
        selected_account=Account.objects.filter(user_id=userid).first()
        queryset=OrderDetail.objects.filter(orderdetail__UserOder_id=selected_account.id,orderdetail__transaction=False,purchase=False)
        return queryset
    def get_context_data(self, *args,**kwargs):
        context=super(CartPage, self).get_context_data(*args,**kwargs)
        userid = self.request.user.id
        selected_account = Account.objects.filter(user_id=userid).first()
        total_price= OrderDetail.objects.filter(orderdetail__UserOder_id=selected_account.id,orderdetail__transaction=False, purchase=False)
        total__price=[]
        for item in total_price:
            total__price.append(item.totalpriceorder)
        context['totalsum']=sum(total__price)
        print(context['totalsum'])
        print("totalsum")
        if context['totalsum']==0:
            context['total']=0
        else:
            context['total']=context['totalsum']-10
        return context

def Removeitem(request,**kwargs):
    productdetailid=kwargs['productdetailid']
    userid=request.user.id
    selected_account=Account.objects.filter(user_id=userid).first()
    selected_order=Order.objects.filter(UserOder_id=selected_account.id,transaction=False).first()
    selected_orderdetail=OrderDetail.objects.filter(orderdetail_id=selected_order.id,productorder_id=productdetailid).delete()
    return redirect("/CartPage")


class CheckCard(DetailView):
    template_name = 'Order/CheckCard.html'
    order_detail=None
    account_sl=None
    order_sl=None
    def setup(self, request, *args, **kwargs):
        super(CheckCard, self).setup(request)
        request=self.request
        args=self.args
        kwargs=self.kwargs
        userid = request.user.id
        self.account_sl = Account.objects.filter(user_id=userid).first()
        self.order_sl = Order.objects.filter(UserOder_id=self.account_sl.id, transaction=False).first()
        if self.order_sl:
            self.order_detail = OrderDetail.objects.filter(orderdetail_id=self.order_sl.id, purchase=False).all()
        else:
            self.order_detail=None
    def dispatch(self, request, *args, **kwargs):
        if request.method=="POST":
            self.post(request)
            return redirect("/DashboardPage")
        if self.order_detail is None:
            return redirect("/")
        else:
            return self.get(request)
    def get_object(self, queryset=None):
        queryset=self.order_detail
        return queryset
    def post(self, request, *args, **kwargs):
        print("enter post")
        deliveryform=ShippingForm(data=self.request.POST or None)
        CardDetail=CreditCardForm(data=self.request.POST or None)
        if(deliveryform.is_valid() and CardDetail.is_valid()):
            firstname=deliveryform.cleaned_data['firstname']
            lastname=deliveryform.cleaned_data['lastname']
            email=deliveryform.cleaned_data['email']
            phone=deliveryform.cleaned_data['phone']
            zip=deliveryform.cleaned_data['zip']
            house=deliveryform.cleaned_data['house']
            building=deliveryform.cleaned_data['building']
            street=deliveryform.cleaned_data['street']
            state=deliveryform.cleaned_data['state']
            postalcode=deliveryform.cleaned_data['postalcode']
            cardnumber=CardDetail.cleaned_data['cardnumber']
            cardmonth=CardDetail.cleaned_data['card_month']
            cardcsv=CardDetail.cleaned_data['cardcsv']
            cardyear=CardDetail.cleaned_data['card_year']
            orderuser=Order.objects.filter(UserOder__user_id=self.request.user.id,transaction=False).first()
            Create_Shipping = ShippingDetail.objects.create(ShipOrder_id=orderuser.id, firstname=firstname,
                                                           lastname=lastname,
                                                           email=email,
                                                           phone=phone,
                                                           zip=zip, house=house,
                                                           building=building,
                                                           street=street,
                                                           state=state,
                                                           postalcode=postalcode)
            CardSpecification.objects.create(CardOrder_id=orderuser.id,
                                             CardMonth=cardmonth,
                                             CardNumber=cardnumber,
                                             CsvCard=cardcsv,
                                             CardYear=cardyear)
            Order.objects.filter(UserOder__user_id=self.request.user.id,transaction=False).update(transaction=True)



    def get_context_data(self,*args,**kwargs):
        context=super(CheckCard, self).get_context_data(*args,**kwargs)
        userid=self.request.user.id
        account=Account.objects.filter(user_id=userid).first()
        sum_order=OrderDetail.objects.filter(orderdetail__UserOder_id=account.id,orderdetail__transaction=False,purchase=False)
        total_sum=[]
        for item in sum_order:
            total_sum.append(item.totalpriceorder)
        context['totalsum']=sum(total_sum)
        print("cconte")
        print(context['totalsum'])
        if context['totalsum']==0:
            context['finalprice']=0
        else:
            context['finalprice']=context['totalsum']-10
        shippingdetail=ShippingDetail.objects.filter(ShipOrder__UserOder_id=account.id,ShipOrder__transaction=True).first()

        if(shippingdetail):
            initial_data={
                "firstname":shippingdetail.firstname,
                "lastname":shippingdetail.lastname,
                "email":shippingdetail.email,
                "phone":shippingdetail.phone,
                "postalcode":shippingdetail.postalcode,
                "zip":shippingdetail.zip,
                "country":shippingdetail.Country,
                "building":shippingdetail.building,
                "street":shippingdetail.street,
                "state":shippingdetail.state,
                "house":shippingdetail.house
            }
        else:
            initial_data={
                "firstname":self.request.user.username,
                "lastname":self.request.user.last_name,
                "email":self.request.user.email,

            }
        addressform = ShippingForm(initial=initial_data)
        context['CardSpec']=CreditCardForm()
        context['address']=addressform
        return context

def Addcount(request):
    quantity=request.GET.get("quantity")
    productid=request.GET.get("prodcutdetailid")
    userid=request.user.id
    print(quantity)
    OrderDetail.objects.filter(orderdetail__UserOder__user_id=userid,orderdetail__transaction=False,productorder_id=productid).update(order_count=quantity)

def ReduceCount(request):
    quantity = request.GET.get("quantity")
    productid = request.GET.get("prodcutdetailid")
    userid = request.user.id
    OrderDetail.objects.filter(orderdetail__UserOder__user_id=userid, orderdetail__transaction=False,productorder_id=productid).update(order_count=quantity)

def AddtoCart(request):
    totalprice=request.GET.get("totalvalue")
    userid=request.user.id
    OrderSel=Order.objects.filter(UserOder__user_id=userid,transaction=False).update(PriceOrder=totalprice)
    isChecked=False
    if(OrderSel):
        isChecked=True
    Response={
        "isChecked":isChecked
    }
    return JsonResponse(data=Response,safe=False)






