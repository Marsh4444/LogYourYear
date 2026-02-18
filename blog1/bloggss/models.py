from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Category(models.Model):
    """
    This is the categories model(table)
    """
    category_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.category_name 

    class Meta:
        verbose_name_plural = 'categories'


STATUS_CHOICES = (
    ('draft', 'Draft'),
    ('published', 'Published'),
)
    
class Blog(models.Model):
    """
    This is the blog model(table)
    """
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, max_length=200)
    content = models.TextField(max_length=2300)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    blog_image = models.ImageField(upload_to='uploads/%Y/%m/%d')
    short_desc = models.TextField(max_length=500)
    status = models.CharField(max_length=30, choices=STATUS_CHOICES, default="drafted")
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Blog"
        verbose_name_plural = "Blogs"

    def __str__(self):
        return self.title