from django.contrib import admin
from django.urls import path, include

# Root URL configuration for TaskManager project
urlpatterns = [
    path('admin/', admin.site.urls),  # Django admin panel

    # App routes
    path('tasks/', include('tasks.urls')),  # Task management
    path('users/', include('users.urls')),  # User authentication and registration

    # API routes
    path('api/v1/', include('api.urls')),  # Versioned API endpoints
]
