from .models import ProductDetail
from Order.models import OrderDetail
def populare_product(request):
    mostcount=OrderDetail.objects.order_by('order_count')[:3]
    return dict(mostcount=mostcount)

