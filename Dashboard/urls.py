from django.urls import path
from .views import DashBoardPage,ProfileEditPage
urlpatterns=[
    path('DashboardPage',DashBoardPage.as_view()),
    path('EditProfile',ProfileEditPage.as_view())
]