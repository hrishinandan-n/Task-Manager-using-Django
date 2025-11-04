from django.shortcuts import render, redirect

from .models import TaskInfo

from .forms import TaskForm

# Create your views here.
def home(request):
    return render(request, 'home.html')

def listTask(request):
    taskList = TaskInfo.objects.all()
    return render(request, 'listTask.html', {'taskList':taskList})

def addTask(request):
    if request.POST:
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listTask')
    else:
        form = TaskForm()
    
    return render(request, 'addTask.html', {'form':form})

def editTask(request, pk):
    task = TaskInfo.objects.get(pk=pk)
    if request.POST:
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('listTask')
    else:
        form = TaskForm(instance=task)
    
    return render(request, 'editTask.html', {'form':form})

def deleteTask(request, pk):
    task = TaskInfo.objects.get(pk=pk)
    task.delete()
    return redirect('listTask')

