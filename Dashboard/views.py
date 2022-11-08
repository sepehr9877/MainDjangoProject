from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views.generic import DetailView,View,CreateView
from Order.models import Order,OrderDetail,ShippingDetail,CardSpecification
from Order.forms import ShippingForm
from Account.models import Account
from .forms import UpdateProfile
# Create your views here.
class DashBoardPage(DetailView):
    Selected_Order_user=None
    Selected_Order_Detail=None
    template_name = 'dashboard/Dashboard.html'
    def get_object(self, queryset=None):
        userid=self.request.user.id
        self.Selected_Order_user=Order.objects.filter(UserOder__user_id=userid,transaction=True).order_by('OrderDate').first()
        print("Order")
        print(self.Selected_Order_user)
        queryset=OrderDetail.objects.filter(orderdetail_id=self.Selected_Order_user.id).all()
        return queryset
    def get_context_data(self,*args,**kwargs):
        context=super(DashBoardPage, self).get_context_data(*args,**kwargs)
        context['username']=self.request.user.username
        context['shipping']=ShippingDetail.objects.filter(ShipOrder_id=self.Selected_Order_user.id).first()
        context['carddetail']=CardSpecification.objects.filter(CardOrder_id=self.Selected_Order_user.id).first()
        context['total_price']=self.Selected_Order_user
        return context


class ProfileEditPage(DetailView):
    template_name = 'dashboard/EditProfile.html'
    def get(self, request, *args, **kwargs):
        account_detail=Account.objects.filter(user_id=self.request.user.id).first()
        initial_date={
            "username":account_detail.user.username,
            "lastname":self.request.user.last_name,
            "phone":account_detail.phonenumber,
            "email":self.request.user.email
        }
        context={"Profile_Spec":UpdateProfile(initial=initial_date)}
        return render(self.request,template_name=self.template_name,context=context)
    def post(self, request, *args, **kwargs):
        profile_form=UpdateProfile(data=self.request.POST or None)
        userid=self.request.user.id
        if profile_form.is_valid():
            username=profile_form.cleaned_data['username']
            lastname=profile_form.cleaned_data['lastname']
            phone=profile_form.cleaned_data['phone']
            email=profile_form.cleaned_data['email']
            user=User.objects.filter(id=userid).first()
            user.first_name=username
            user.last_name=lastname
            user.email=email
            user.save()
            account=Account.objects.filter(user_id=userid).update(phonenumber=phone)
        return redirect('/EditProfile')
class MyTransactionOrder(DetailView):
    template_name = 'dashboard/TransactionPage.html'
    all_My_Order=None
    def get_object(self, queryset=None):
        userid=self.request.user.id
        selected_account=Account.objects.filter(user_id=userid).first()
        Order_user=Order.objects.filter(UserOder__user_id=userid).all()
        shippingdetail=ShippingDetail.objects.filter(ShipOrder__UserOder_id=selected_account.id)
        print(shippingdetail)
        QuerySet=[]
        for item in Order_user:
            QuerySet.append(OrderDetail.objects.filter(orderdetail_id=item.id))
        queryset=QuerySet
        return queryset