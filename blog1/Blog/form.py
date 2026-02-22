from django import forms
from bloggss.models import Blog, Category  # your Post model

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        exclude = ["author", "slug"]  # exclude fields that should not be edited by the user


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['category_name']