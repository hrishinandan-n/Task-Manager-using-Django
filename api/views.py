from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth import authenticate

from tasks.models import TaskInfo
from api.serializers import LoginSerializer, RegisterSerializer, TaskInfoSerializer


class TaskPagination(PageNumberPagination):
    """Custom pagination with fixed page size."""
    page_size = 5


class TaskInfoViewSet(viewsets.ModelViewSet):
    """CRUD API for TaskInfo model with authentication and pagination."""
    queryset = TaskInfo.objects.all()
    serializer_class = TaskInfoSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = TaskPagination

    def perform_create(self, serializer):
        """Attach logged-in user when creating a new task."""
        serializer.save(user=self.request.user)


class RegisterAPI(APIView):
    """Handle user registration."""
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({"message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response({"message": "User created successfully"}, status=status.HTTP_201_CREATED)


class LoginAPI(APIView):
    """Authenticate user and return auth token."""
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({"message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

        user = authenticate(
            username=serializer.validated_data['username'],
            password=serializer.validated_data['password']
        )

        if not user:
            return Response({"message": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)

        token, _ = Token.objects.get_or_create(user=user)
        return Response({'message': 'Login successful', 'token': str(token)}, status=status.HTTP_200_OK)
