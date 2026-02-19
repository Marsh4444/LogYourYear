from django.shortcuts import render, get_object_or_404
from .models import Category, Blog 

# Create your views here.
def category_posts(request, pk):
    posts = Blog.objects.filter(category=pk, status='published').order_by('-updated_at')
    category = get_object_or_404(Category, pk=pk)

    context = {
        'posts': posts,
        'category': category,
    }

    return render(request, 'category_posts.html', context)


def single_blogs(request, blog_slug):
    single_post = get_object_or_404(Blog, slug=blog_slug, status='published')
    context = {
        'single_post' : single_post
    }

    return render(request, 'single_blogs.html', context)


