from django.urls import path
from .views import Addcount,CreatingOrder,CartPage,Removeitem,CheckCard,ReduceCount
urlpatterns=[
    path('CreatingOrder/',CreatingOrder.as_view()),
    path('CartPage',CartPage.as_view()),
    path('Remove/<productdetailid>',Removeitem),
    path("CheckCard",CheckCard.as_view()),
    path("Addcount/",Addcount),
    path("ReduceCount/",ReduceCount)

]