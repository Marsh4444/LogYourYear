from django.shortcuts import get_object_or_404, redirect, render
from .models import Task
# Create your views here.

def addTask(request):
    # Logic to add a task goes here
    task = request.POST['task']  # Example of accessing the task data from the form
    Task.objects.create(task=task)  # Save the new task to the database
    return redirect('home')  # Redirect to the home page after adding the task

def markComplete(request, pk):
    # Logic to mark a task as complete goes here
    task = get_object_or_404(Task, pk=pk)
    task.is_completed = True
    task.save()
    return redirect('home')  # Redirect to the home page after marking the task as complete

def markIncomplete(request, pk):
    # Logic to mark a task as incomplete goes here
    task = get_object_or_404(Task, pk=pk)
    task.is_completed = False
    task.save()
    return redirect('home')  # Redirect to the home page after marking the task as incomplete

def editTask(request, pk):
    # Logic to edit a task goes here
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.task = request.POST['task']  # Update the task with new data from the form
        task.save()
        return redirect('home')  # Redirect to the home page after editing the task
    return render(request, 'todo/edit_task.html', {'task': task})  # Render the edit task template

def deleteTask(request, pk):
    # Logic to delete a task goes here
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('home')  # Redirect to the home page after deleting the task