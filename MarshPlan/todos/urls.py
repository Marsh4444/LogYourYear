"""
Todo URL Configuration
----------------------
This module defines URL patterns for the todos application.
Maps URLs to their corresponding view functions.

URL patterns:
- / : List all todos (main page)
- /todo/<id>/ : View details of a specific todo
- /create/ : Create a new todo
- /todo/<id>/update/ : Edit an existing todo
- /todo/<id>/toggle/ : Toggle completion status
- /todo/<id>/delete/ : Delete a todo
"""

from django.urls import path
from . import views

# URL patterns for the todos app
urlpatterns = [
    # Display all todos
    # URL: /
    # Name: 'todo_list'
    path('', views.home, name='home'),
    
    # Display a specific todo's details
    # URL: /todo/<int:pk>/
    # Name: 'todo_detail'
    # Parameters: pk (integer) - the todo's primary key (id)
    path('todo/<int:pk>/', views.todo_detail, name='todo_detail'),
    
    # Show form to create a new todo
    # URL: /create/
    # Name: 'todo_create'
    path('create/', views.todo_create, name='todo_create'),
    
    # Show form to edit an existing todo
    # URL: /todo/<int:pk>/update/
    # Name: 'todo_update'
    # Parameters: pk (integer) - the todo's primary key (id)
    path('todo/<int:pk>/update/', views.todo_update, name='todo_update'),
    
    # Toggle the completion status of a todo
    # URL: /todo/<int:pk>/toggle/
    # Name: 'todo_toggle'
    # Parameters: pk (integer) - the todo's primary key (id)
    path('todo/<int:pk>/toggle/', views.todo_toggle, name='todo_toggle'),
    
    # Delete a todo (POST only)
    # URL: /todo/<int:pk>/delete/
    # Name: 'todo_delete'
    # Parameters: pk (integer) - the todo's primary key (id)
    path('todo/<int:pk>/delete/', views.todo_delete, name='todo_delete'),
]

