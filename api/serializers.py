from rest_framework import serializers
from django.contrib.auth.models import User
from tasks.models import TaskInfo


class UserSerializer(serializers.ModelSerializer):
    """Serializer for Django's built-in User model (limited to username)."""
    class Meta:
        model = User
        fields = ['username']


class TaskInfoSerializer(serializers.ModelSerializer):
    """Serializer for TaskInfo model, including read-only user data."""
    user = UserSerializer(read_only=True)

    class Meta:
        model = TaskInfo
        fields = ['id', 'title', 'description', 'due_date', 'user']
        depth = 1


class RegisterSerializer(serializers.Serializer):
    """Serializer for user registration with validation for duplicates."""
    username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        """Check for existing username and email before creating a new user."""
        if User.objects.filter(username=data['username']).exists():
            raise serializers.ValidationError("Username already exists.")
        if User.objects.filter(email=data['email']).exists():
            raise serializers.ValidationError("Email already exists.")
        return data

    def create(self, validated_data):
        """Create a new user instance with hashed password."""
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user


class LoginSerializer(serializers.Serializer):
    """Serializer for handling user login authentication."""
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
