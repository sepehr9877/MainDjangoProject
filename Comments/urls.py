from django.urls import path
from .views import AddingComment
urlpatterns=[
    path('AddComment/<int:ID>',AddingComment.as_view())
]