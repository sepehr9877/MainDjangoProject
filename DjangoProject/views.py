from django.shortcuts import render

from Categories.models import Category


def homepage(request):
    return render(request,"homepage.html")