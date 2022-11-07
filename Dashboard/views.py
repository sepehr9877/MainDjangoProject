from django.shortcuts import render
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
        queryset=OrderDetail.objects.filter(orderdetail__UserOder__user_id=self.Selected_Order_user.id).all()
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
    # def get_context_data(self, *args,**kwargs):
    #     context=super(ProfileEditPage, self).get_context_data(*args,**kwargs)
    #     context['EditProfile']=UpdateProfile()
    #     return context
