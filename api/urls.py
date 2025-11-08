from django.urls import include, path
from . import views


urlpatterns = [
    path('taskInformation/', views.taskInformation, name='taskInformation'),
    path('RegisterAPI/', views.RegisterAPI.as_view(), name='RegisterAPI'),
    path('LoginAPI/', views.LoginAPI.as_view(), name='LoginAPI'),
    # path('listTask/<pk>/', views.userTask, name='userTask'),
]
 
 
#  for class-based view
# urlpatterns = [     
#     path('TaskInformationClass/', views.TaskInformationClass.as_view(), name='TaskInformationClass'),      
#  ]
    
    

# Routers
# from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register(r'TaskInfoViewSet', views.TaskInfoViewSet, basename='TaskInfoViewSet')
# urlpatterns = router.urls

# urlpatterns = [
#     path('TaskInfoViewSet/', include(router.urls))
# ]