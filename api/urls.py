from django.urls import path, include
from .views import ProfileView

urlpatterns = [
    path('profileView/', ProfileView.as_view(), name='profileView')
]