from django.urls import path
from tasks import views

# URL patterns mapping paths to view functions
urlpatterns = [
    path('home/', views.home, name='home'),  # Home page
    path('addTask/', views.addTask, name='addTask'),  # Add a new task
    path('editTask/<pk>/', views.editTask, name='editTask'),  # Edit task by ID
    path('deleteTask/<pk>/', views.deleteTask, name='deleteTask'),  # Delete task by ID
    path('listTask/', views.listTask, name='listTask'),  # List all user tasks
]
