from django.shortcuts import render
from bloggss.models import Blog
from django.db.models import Q


def home(request):
    """ Logic for the home page"""

    featured_posts = Blog.objects.filter(is_featured=True, status='published').order_by('-updated_at')
    blogs = Blog.objects.filter(status='published', is_featured=False).order_by('-updated_at')
    context = {
        'featured_posts': featured_posts,
        'blogs': blogs,
    }

    return render(request, 'home.html', context)


def search(request):
    keyword = request.GET.get('keyword')
    blogs = Blog.objects.filter(Q(title__icontains=keyword) | Q(short_desc__icontains=keyword) | Q(content__icontains=keyword)).order_by('-updated_at')

    context = {
        'keyword': keyword,
        'blogs' : blogs,
    }
    return render(request, 'search.html', context)
