from django import forms

from .models import TaskInfo

class TaskForm(forms.ModelForm):
    class Meta:
        model = TaskInfo
        fields = ['content']