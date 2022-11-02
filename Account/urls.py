from django.urls import path
from .views import RegisterPage,LoginPage
urlpatterns=[
    path("Registration",RegisterPage.as_view()),
    path("LoginPage",LoginPage.as_view())

]