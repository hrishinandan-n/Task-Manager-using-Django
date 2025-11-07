from rest_framework import serializers
from tasks.models import TaskInfo

class TaskInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskInfo
        fields = ['title', 'description', 'due_date']