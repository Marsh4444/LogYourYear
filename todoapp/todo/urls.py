from django.urls import path
from . import views

urlpatterns = [
    # Define your todo app URL patterns here
    path('addTask/', views.addTask, name='addTask'),
    # Mark Complete Task
    path('markComplete/<int:pk>/', views.markComplete, name='markComplete'),
    # Mark Incomplete Task
    path('markIncomplete/<int:pk>/', views.markIncomplete, name='markIncomplete'),
    #Edit Task
    path('editTask/<int:pk>/', views.editTask, name='editTask'),
    #Delete Task
    path('deleteTask/<int:pk>/', views.deleteTask, name='deleteTask'),
]