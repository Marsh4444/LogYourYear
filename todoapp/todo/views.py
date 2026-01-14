from django.shortcuts import redirect, render
from .models import Task
# Create your views here.

def addTask(request):
    # Logic to add a task goes here
    task = request.POST['task']  # Example of accessing the task data from the form
    Task.objects.create(task=task)  # Save the new task to the database
    return redirect('home')  # Redirect to the home page after adding the task
