from django.contrib.auth.models import User
from django.db.models import Count

from Order.models import OrderDetail
from Account.models import Account

def orderusercount(request):
    userid = request.user.id
    orderscount = OrderDetail.objects.filter(orderdetail__UserOder__user_id=userid,
                                             orderdetail__transaction=False).aggregate(
        userordercount=Count('productorder'))
    return dict(count=orderscount['userordercount'])

