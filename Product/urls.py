from django.urls import path
from .views import searchview
urlpatterns=[
    path('Search/',searchview.as_view())
]