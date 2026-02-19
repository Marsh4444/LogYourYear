from django.urls import  path
from Blog import views as Blogsview
from . import views


urlpatterns = [
    #path('', views.home, name='home'),
    path('category/<int:pk>/', views.category_posts, name ='category_posts' ),
    path('blogs/<slug:blog_slug>/', views.single_blogs, name='single_blogs'),
    path('search/', Blogsview.search, name='search'),
]