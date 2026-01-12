from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def addTask(request):
    if request.method == 'POST':
        task_content = request.POST.get('task')
        # Here you would typically save the task to the database
        # For now, we will just redirect back to home
    return render(request, 'home.html')