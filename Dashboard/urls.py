from django.urls import path
from .views import DashBoardPage
urlpatterns=[
    path('DashboardPage',DashBoardPage.as_view())
]