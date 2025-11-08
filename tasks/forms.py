# 💭 Model forms and formsets.
import datetime
from django import forms

from .models import TaskInfo


class TaskForm(forms.ModelForm):
    class Meta:
        model = TaskInfo
        fields = ['title', 'description', 'due_date']
    
    def clean_due_date(self):
        due_date = self.cleaned_data.get('due_date')
        if due_date and due_date < datetime.date.today():
            raise forms.ValidationError("Due date cannot be in the past.")
        return due_date