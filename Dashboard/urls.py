from django.urls import path
from .views import DashBoardPage,ProfileEditPage,MyTransactionOrder
urlpatterns=[
    path('DashboardPage',DashBoardPage.as_view()),
    path('EditProfile',ProfileEditPage.as_view()),
    path('MyTransactionOrder',MyTransactionOrder.as_view())
]