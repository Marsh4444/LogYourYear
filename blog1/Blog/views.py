from django.shortcuts import render
from bloggss.models import Category


def home(request):
    """ Logic for the home page"""
    categories = Category.objects.all()
    context = {
        'categories' : categories
    }

    return render(request, 'home.html', context)