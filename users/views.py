from django.shortcuts import render, redirect

# 💭User model 
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


# Create your views here.

# 💭 Creating user registration and login forms. 
def createUser(request):
    user = None
    error_msg = None 
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.create_user(username=username, password=password)
            return redirect('loginUser')
        except Exception as e:
            error_msg = str(e)
    return render(request, 'users/signUp.html', {'user': user, 'error':error_msg})

def loginUser(request):
    error_msg = None
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('listTask')
        
    return render(request, 'users/loginUser.html' )

def logoutUser(request):
    if request:
        logout(request)
        return redirect('loginUser')