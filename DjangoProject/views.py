from django.db.models import Count
from django.shortcuts import render
from Order.models import OrderDetail
def homepage(request):
    return render(request,"homepage.html")
def header(request):
    if request.user.is_authenticated:
        context={"user":request.user.username}
    else:
        context={}

    return render(request,'header/Header.html',context)