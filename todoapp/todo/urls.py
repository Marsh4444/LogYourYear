from django.urls import path
from . import views

urlpatterns = [
    # Define your todo app URL patterns here
    path('addTask/', views.addTask, name='addTask'),
]