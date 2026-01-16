"""
Todo Views
----------
This module contains all view functions for the todos application.
Each view handles a specific HTTP request and returns an appropriate response.

Views included:
- todo_list: Display all todos with completion statistics
- todo_detail: Show detailed view of a single todo
- todo_create: Handle creation of new todos
- todo_update: Handle editing existing todos
- todo_toggle: Toggle completion status of a todo
- todo_delete: Handle deletion of todos
"""

from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods
from .models import Todo


def home(request):
    """
    Display all todos with completion statistics.
    
    This is the main view that shows a list of all todos along with
    statistics about how many have been completed.
    
    Args:
        request: The HTTP request object
        
    Returns:
        HttpResponse: Rendered todo_list.html template with todos and stats
    """
    # Retrieve all todos from the database, ordered by creation date (newest first)
    todos = Todo.objects.all()
    
    # Count how many todos are marked as completed
    completed_count = todos.filter(completed=True).count()
    
    # Get total number of todos
    total_count = todos.count()
    
    # Prepare context data to pass to the template
    context = {
        'todos': todos,  # All todos for iteration in template
        'completed_count': completed_count,  # Number of completed todos
        'total_count': total_count,  # Total number of todos
    }
    
    # Render and return the template with context data
    return render(request, 'todos/home.html', context)


def todo_detail(request, pk):
    """
    Display detailed information about a single todo.
    
    Retrieves a specific todo by its primary key (id) and shows all
    details including title, description, due date, and timestamps.
    Returns a 404 error if the todo does not exist.
    
    Args:
        request: The HTTP request object
        pk (int): Primary key (id) of the todo to display
        
    Returns:
        HttpResponse: Rendered todo_detail.html template with todo data
        HttpResponse: 404 error if todo does not exist
    """
    # Get the todo by primary key, or return 404 if not found
    todo = get_object_or_404(Todo, pk=pk)
    
    # Render and return the detail template with the todo
    return render(request, 'todos/todo_detail.html', {'todo': todo})


def todo_create(request):
    """
    Create a new todo from form submission.
    
    Handles both GET requests (show the form) and POST requests (process form data).
    On POST, validates that title is provided, creates a new Todo object,
    and saves it to the database. Redirects to todo_list on success.
    
    Args:
        request: The HTTP request object
        
    Returns:
        HttpResponse: Rendered todo_form.html template on GET
        HttpResponseRedirect: Redirect to todo_list after successful creation
    """
    if request.method == 'POST':
        # Extract form data from POST request
        title = request.POST['title']  # Required field
        description = request.POST['description']  # Optional field
        due_date = request.POST['due_date']  # Optional field

        # Validate that title is provided (required for todos)
        if title:
            # Create a new Todo object with title and description
            todo = Todo(title=title, description=description)
            
            # If due date was provided, add it to the todo
            if due_date:
                todo.due_date = due_date
            
            # Save the todo to the database
            todo.save()
            
            # Redirect to the todo list view after successful creation
            return redirect('home')
    
    # For GET requests, render the form template (form will be empty)
    return render(request, 'todos/todo_form.html')


def todo_update(request, pk):
    """
    Update an existing todo.
    
    Handles both GET requests (show the form pre-filled with existing data)
    and POST requests (process updated form data). On POST, updates the todo
    with new values and saves to database. Redirects to todo_detail on success.
    
    Args:
        request: The HTTP request object
        pk (int): Primary key (id) of the todo to update
        
    Returns:
        HttpResponse: Rendered todo_form.html template with pre-filled data on GET
        HttpResponseRedirect: Redirect to todo_detail after successful update
        HttpResponse: 404 error if todo does not exist
    """
    # Get the todo by primary key, or return 404 if not found
    todo = get_object_or_404(Todo, pk=pk)
    
    if request.method == 'POST':
        # Update title, or keep existing if not provided
        todo.title = request.POST['title']
        
        # Update description, or keep existing if not provided
        todo.description = request.POST['description']
        
        # Update due date, or set to None if not provided
        todo.due_date = request.POST['due_date'] or None
        
        # Save the updated todo to the database
        todo.save()
        
        # Redirect to the todo detail page after successful update
        return redirect('todo_detail', pk=pk)
    
    # For GET requests, render the form with existing todo data pre-filled
    context = {'todo': todo}
    return render(request, 'todos/todo_form.html', context)


def todo_toggle(request, pk):
    """
    Toggle the completion status of a todo.
    
    Switches the completed state of a todo between True and False.
    Useful for marking todos as done or undoing completion.
    
    Args:
        request: The HTTP request object
        pk (int): Primary key (id) of the todo to toggle
        
    Returns:
        HttpResponseRedirect: Redirect to todo_list after toggle
        HttpResponse: 404 error if todo does not exist
    """
    # Get the todo by primary key, or return 404 if not found
    todo = get_object_or_404(Todo, pk=pk)
    
    # Toggle the completed status (True -> False, False -> True)
    todo.completed = not todo.completed
    
    # Save the updated status to the database
    todo.save()
    
    # Redirect back to the todo list
    return redirect('home')


@require_http_methods(['POST'])
def todo_delete(request, pk):
    """
    Delete a todo from the database.
    
    Permanently removes a todo. This view only accepts POST requests
    for security (to prevent accidental deletion via GET requests).
    
    Args:
        request: The HTTP request object (must be POST)
        pk (int): Primary key (id) of the todo to delete
        
    Returns:
        HttpResponseRedirect: Redirect to todo_list after deletion
        HttpResponse: 404 error if todo does not exist
        HttpResponse: 405 error if not a POST request
    """
    # Get the todo by primary key, or return 404 if not found
    todo = get_object_or_404(Todo, pk=pk)
    
    # Permanently delete the todo from the database
    todo.delete()
    
    # Redirect back to the todo list
    return redirect('home')
