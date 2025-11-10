from django.contrib import admin
from django.http import HttpResponse
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView ,SpectacularSwaggerView


def home(request):
    return HttpResponse("Welcome to Task Manager")

# Root URL configuration for TaskManager project
urlpatterns = [
    path('admin/', admin.site.urls),  # Django admin panel

    # App routes
    path('tasks/', include('tasks.urls')),  # Task management
    path('users/', include('users.urls')),  # User authentication and registration
    path('', home), # Root URL

    # API routes

    path('api/v1/', include('api.urls')),  # Versioned API endpoints

    # path('api/v1', include('api.urls')),  # Versioned API endpoints


    # API Schema & Interactive Docs
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),  # Generates OpenAPI schema (YAML/JSON)
    path('api/schema/docs/', SpectacularSwaggerView.as_view(url_name='schema')),  # Swagger UI
]

