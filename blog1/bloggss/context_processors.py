from .models import Category
from assign.models import About, FollowUs


def get_categories(request):
    categories = Category.objects.all().order_by('-updated_at')
    return {'categories': categories}


def about_us(request):
    abouts = About.objects.get()
    return {'abouts': abouts}


def get_follow_us(request):
    follow_us_links = FollowUs.objects.all()
    return {'follow_us_links': follow_us_links}