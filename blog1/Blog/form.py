from django import forms
from bloggss.models import Blog  # your Post model

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        exclude = ["author", "slug"]  # exclude fields that should not be edited by the user