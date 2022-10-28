from django.core.paginator import Paginator
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
    def get_queryset(self):
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

        context['pro_cat']=ProductDetail.objects.filter(id=self.ID)._values('Pro_size__SizeRate')
        print(ProductDetail.objects.filter(id=self.ID).values('Pro_size__SizeRate'))
        return context