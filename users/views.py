from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

def createUser(request):
    """Handle new user registration."""
    user, error_msg = None, None
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = User.objects.create_user(username=username, password=password)
            return redirect('loginUser')
        except Exception as e:
            error_msg = str(e)
    return render(request, 'users/signUp.html', {'user': user, 'error': error_msg})

def loginUser(request):
    """Authenticate and log in an existing user."""
    error_msg = None
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            request.session['username'] = username
            return redirect('listTask')
        error_msg = "Invalid credentials"
    return render(request, 'users/loginUser.html', {'error': error_msg})

def logoutUser(request):
    """Log out the current user and redirect to login."""
    logout(request)
    return redirect('loginUser')
