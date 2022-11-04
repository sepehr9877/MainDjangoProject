import json
from json import dumps

from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView, TemplateView, DetailView

from Categories.models import Category
from Product.models import Product,ProductDetail
from SizeColor.models import Colors,Sizes
# Create your views here.
class searchview(ListView):
    model = ProductDetail
    template_name = 'SearchResult/SearchResult.html'
    paginate_by = 3
    count=None
    SearchFilter=None
    def get_queryset(self):
        if( self.SearchFilter):
            return self.SearchFilter
        name=self.request.GET.get('q')

        if name is None:
            self.count=ProductDetail.objects.all().count()
            return ProductDetail.objects.all()
        else:
            self.count=ProductDetail.objects.Searhcitem(name).count()
            return ProductDetail.objects.Searhcitem(name)


    def get_context_data(self, *args, **kwargs):
        context=super(searchview,self).get_context_data(*args,**kwargs)
        categories=Category.objects.filter(Parentitem=None).distinct()
        SizeRates=Sizes.objects.all().distinct()
        context['Categories']=categories
        context['SizeRates']=SizeRates
        context['Counts']=self.count
        return context
class CategorySearch(ListView):
    paginate_by = 3
    template_name = 'SearchResult/SearchResult.html'
    model = ProductDetail
    slugvalue=None
    count=None
    def get_queryset(self):
        self.slugvalue=None
        categoryname=self.get_slug_value()
        print(categoryname)
        Product_Category = ProductDetail.objects.filter(Pro_Cat__ParentCategory__icontains=categoryname)
        if len(Product_Category)==0:
            print("Product_Category")
            Product_Category=ProductDetail.objects.filter(Pro_Cat__Parentitem__ParentCategory=categoryname)
        self.count=Product_Category.count()
        return Product_Category
    def get_slug_value(self):
        self.slugvalue=self.kwargs['CategoryName']
        return self.slugvalue
    def get_context_data(self,*args,**kwargs):
        context=super(CategorySearch, self).get_context_data(*args,**kwargs)
        categories = Category.objects.filter(Parentitem=None).distinct()
        SizeRates=Sizes.objects.all().distinct()
        print(SizeRates)
        context['Categories'] = categories
        context['SizeRates'] = SizeRates
        context['Counts'] = self.count
        return context
class ProductDetailView(DetailView):
    template_name = 'DetailView/DetailView.html'
    slug_field = 'int'
    slug_url_kwarg = 'ID'
    model = ProductDetail
    ID=None

    def get_object(self, queryset=None):
        self.ID=self.kwargs[self.slug_url_kwarg]
        queryset=ProductDetail.objects.filter(id=self.ID).first()
        return queryset
    def get_context_data(self,*args, **kwargs):
        context=super(ProductDetailView, self).get_context_data(*args,**kwargs)
        productid=ProductDetail.objects.filter(id=self.ID).values('Pro_Detail_id')

        print(productid)
        p_id=[]
        for item in productid:
            for key in item:
                p_id.append(item.get(key))
        selected_size=ProductDetail.objects.filter(Pro_Detail_id=p_id[0]).values('Pro_size__SizeRate')
        selected_size_list=[]
        for item in selected_size:
            for key in item:
                selected_size_list.append(item.get(key))
        context['pro_sizes']=selected_size_list
        selected_color=ProductDetail.objects.filter(Pro_Detail_id=p_id[0]).values('Pro_color__Color_Rate')
        color_rates=[]
        for item in selected_color:
            for key in item:
                color_rates.append(item.get(key))
        context['color_rates']=set(color_rates)
        print(color_rates)
        return context
class Filtering(DetailView):
    template_name = 'DetailView/DetailView.html'
    sizeJ=None
    def get(self, request, *args, **kwargs):
        color=self.request.GET.get('color')
        ProductID=self.request.GET.get('ProductID')
        SelectedSize=ProductDetail.objects.filter(Pro_Detail_id=ProductID,Pro_color__Color_Rate=color).values_list('Pro_size__SizeRate')
        listsize=list(SelectedSize)
        JsonData=dumps(listsize)
        data={
            "sizerange":JsonData
        }
        print(JsonData)
        return JsonResponse(data,safe=False)



class SearchBySize(DetailView):
    def get(self, request, *args, **kwargs):
        pricerange=self.request.GET.get('max_price')
        size=self.request.GET.get('size')
        userid=self.request.user.id
        print(size,pricerange)
        selected_product=ProductDetail.objects.filter(Pro_size__SizeRate=size,Pro_Detail__price__lte=pricerange).values_list('id')
        selected_product=list(selected_product)
        id_selected=[item[0] for item in selected_product ]
        selected_product=dumps(id_selected)
        data={
            "selected_products":selected_product
        }
        return JsonResponse(data,safe=False)
def AssignQuerytoSearch(request):
    ProductsIDList=request.GET.get('ProductsList')
    print("ProductsId")
    print(ProductsIDList)
    mylist=ProductsIDList.strip('][').split(',')
    print(mylist)
    print("mylist")
    print(mylist[0])
    listQuerySet=[]
    for item in mylist:
        listQuerySet.append(ProductDetail.objects.get(id=int(item)))
    searchview.SearchFilter=listQuerySet
    return redirect("/Search/")
    data={
        "isAssigned":True
    }
    return JsonResponse(data,safe=False)