from django.urls import path
from .views import CreatingOrder,CartPage,Removeitem,CheckCard
urlpatterns=[
    path('CreatingOrder/',CreatingOrder.as_view()),
    path('CartPage',CartPage.as_view()),
    path('Remove/<productdetailid>',Removeitem),
    path("CheckCard",CheckCard.as_view())
]