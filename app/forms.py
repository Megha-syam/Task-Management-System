# forms.py

from django import forms
from .models import taskshow

class TaskForm(forms.ModelForm):
    class Meta:
        model = taskshow
        fields = ['name', 'description', 'deadline', 'subject']
