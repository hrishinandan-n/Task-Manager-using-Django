from django.db import models
from django.contrib.auth.models import User

class TaskInfo(models.Model):
    """Represents a task assigned to a specific user."""
    title = models.CharField(max_length=100)  # Short task title
    description = models.TextField(blank=True)  # Optional details
    due_date = models.DateField(null=True, blank=True)  # Optional deadline
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks', null=True)  # Task owner

    def __str__(self):
        """Readable string representation."""
        return f"{self.title} {self.description} {self.due_date} {self.user}"
