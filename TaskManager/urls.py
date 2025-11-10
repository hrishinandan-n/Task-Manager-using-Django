from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView ,SpectacularSwaggerView

# Root URL configuration for TaskManager project
urlpatterns = [
    path('admin/', admin.site.urls),  # Django admin panel

    # App routes
    path('tasks/', include('tasks.urls')),  # Task management
    path('users/', include('users.urls')),  # User authentication and registration

    # API routes
    path('', include('api.urls')),  # Versioned API endpoints

    # API Schema & Interactive Docs
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),  # Generates OpenAPI schema (YAML/JSON)
    path('api/schema/docs', SpectacularSwaggerView.as_view(url_name='schema')),  # Swagger UI
]
