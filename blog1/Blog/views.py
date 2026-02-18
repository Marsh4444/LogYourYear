from django.shortcuts import render
from bloggss.models import Blog


def home(request):
    """ Logic for the home page"""

    featured_posts = Blog.objects.filter(is_featured=True, status='published').order_by('-updated_at')
    blogs = Blog.objects.filter(status='published', is_featured=False).order_by('-updated_at')
    context = {
        'featured_posts': featured_posts,
        'blogs': blogs,
    }

    return render(request, 'home.html', context)