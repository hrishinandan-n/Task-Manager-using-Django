from django.shortcuts import render, redirect

from .models import TaskInfo
from .forms import TaskForm

from django.contrib.auth.decorators import login_required
# Create your views here.

# 💭 Function-based views (FBVs). 
@login_required(login_url='loginUser')
def home(request):
    return render(request, 'home.html')

@login_required(login_url='loginUser')
def listTask(request):
    taskList = TaskInfo.objects.all()
    return render(request, 'listTask.html', {'taskList':taskList})

@login_required(login_url='loginUser')
def addTask(request):
    if request.POST:
        # 💭 Step 1: Create a form class in forms.py.
        # 💭 Step 2: Use the form in a view in views.py
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listTask')
    else:
        form = TaskForm()
    
    return render(request, 'addTask.html', {'form':form})

@login_required(login_url='loginUser')
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

@login_required(login_url='loginUser') 
def deleteTask(request, pk):
    task = TaskInfo.objects.get(pk=pk)
    task.delete()
    return redirect('listTask')

