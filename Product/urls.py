from django.urls import path
from .views import ResultPage
urlpatterns=[
    path('Result',ResultPage)
]