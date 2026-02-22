from django.urls import  path
from Blog import views as Blogsview
from . import views

urlpatterns = [
    path('users/register/', views.register, name='register'),
    path('users/login/', views.login_view, name='login'),
    path('users/logout/', views.logout_view, name='logout'),
    path('users/manager/dashboard/', views.manager_dashboard, name='manager_dashboard'),
    path('users/editor/dashboard/', views.editor_dashboard, name='editor_dashboard'),
    path('users/author/dashboard/', views.author_dashboard, name='author_dashboard'),

    #posts CRUD
    path('users/posts/', Blogsview.posts_list, name='posts_list'),
    path('users/posts/create/', Blogsview.post_create, name='post_create'),
    path('users/posts/<int:pk>/edit/', Blogsview.post_update, name='post_update'),
    path('users/posts/<int:pk>/delete/', Blogsview.post_delete, name='post_delete'),
    #system_reports
    path("users/reports/", Blogsview.system_reports, name="system_reports"),
]