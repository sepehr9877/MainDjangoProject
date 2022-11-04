from django.urls import path
from .views import searchview,CategorySearch,ProductDetailView,Filtering,SearchBySize,AssignQuerytoSearch
urlpatterns=[
    path('Search/',searchview.as_view(),name="Search"),
    path('Category/<slug:CategoryName>',CategorySearch.as_view(),name="CategorySearch"),
    path('ProductDetail/<int:ID>',ProductDetailView.as_view(),name="ProductDetailView"),
    path("Filtering/",Filtering.as_view()),
    path('SearchBySize/',SearchBySize.as_view()),
    path('AssignQuerytoSearch/',AssignQuerytoSearch)
]