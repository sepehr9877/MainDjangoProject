from django.urls import path
from .views import CreatingOrder,CartPage
urlpatterns=[
    path('CreatingOrder/',CreatingOrder.as_view()),
    path('CartPage',CartPage.as_view())
]