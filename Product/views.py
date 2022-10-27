from django.core.paginator import Paginator
from django.shortcuts import render
from Categories.models import Category
from Product.models import Product,ProductDetail
# Create your views here.
def ResultPage(request):

    ParentCategory=Category.objects.filter(Parentitem=None)
    SizeRange=Product.objects.get_valueslist(Product.objects.values('ProSize'))
    Products=ProductDetail.objects.all().distinct()
    paginator=Paginator(Products,3)
    page=request.GET.get('page')
    paged_product=paginator.get_page(page)
    product_count=Products.count()
    context={"ParentCategory":ParentCategory,
             "SizeRanges":SizeRange,
             "Prodcuts":paged_product}
    return render(request,'SearchResult/SearchResult.html',context)