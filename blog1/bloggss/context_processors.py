from .models import Category


def get_categories(request):
    categories = Category.objects.all().order_by('-updated_at')
    return {'categories': categories}