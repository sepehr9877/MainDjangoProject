from django.urls import path
from .views import Registration,LoginPage
urlpatterns=[
    path("Registration",Registration),
    path("LoginPage",LoginPage.as_view())

]