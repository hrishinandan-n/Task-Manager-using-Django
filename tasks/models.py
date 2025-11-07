from django.db import models
from django.contrib.auth.models import User

# Creating your models here. 

# 💭 Creating and defining models. 
class TaskInfo(models.Model):
    # 💭 Fields and field types. 
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    due_date = models.DateField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks', null=True)
    
    # 💭 Model methods. 
    def __str__(self):
        return f"{self.title} {self.description} {self.due_date} {self.completed}"