from django.contrib.auth.models import User
from django.db.models import Count
from django.shortcuts import render
from Order.models import OrderDetail
def homepage(request):
    User.objects.filter(username="jack").delete()
    return render(request,"homepage.html")
def Header(request):
    print("iidddd")
    print(request.user.id)
    selected_account=None
    if User.is_authenticated:
        userid=request.user.id
        selected_account=User.objects.filter(id=userid).values_list('username')
        # selected_account=Account.objects.filter(user_id=userid).values_list('user__username')
        print(selected_account[0])
    else:
        user=None
    return render(request,template_name='header/Header.html',context={"user":selected_account[0][0]})