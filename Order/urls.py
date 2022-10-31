from django.urls import path
from .views import CreatingOrder,Creating
urlpatterns=[
    path('CreatingOrder/',CreatingOrder.as_view()),
    path('Creating/',Creating)
]