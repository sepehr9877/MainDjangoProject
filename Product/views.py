from django.core.paginator import Paginator
from django.shortcuts import render
from django.views.generic import ListView,TemplateView

from Categories.models import Category
from Product.models import Product,ProductDetail
# Create your views here.
class searchview(ListView):
    model = ProductDetail
    template_name = 'SearchResult/SearchResult.html'
    paginate_by = 3
    count=None
    def get_queryset(self):
        if self.request.GET:
            name=self.request.GET.get('q')
            results=ProductDetail.objects.Searhcitem(name)
            self.count=results.count()
            return results
        return ProductDetail.objects.all()
    

# def ResultPage(request):
#
#     ParentCategory=Category.objects.filter(Parentitem=None)
#     SizeRange=Product.objects.get_valueslist(Product.objects.values('ProSize'))
#     Products=ProductDetail.objects.all().distinct()
#     paginator=Paginator(Products,3)
#     page=request.GET.get('page')
#     paged_product=paginator.get_page(page)
#     product_count=Products.count()
#
#     context={"ParentCategory":ParentCategory,
#              "SizeRanges":SizeRange,
#              "page_obj":paged_product}
#     return render(request,'SearchResult/SearchResult.html',context)