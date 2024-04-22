from ast import mod
from turtle import title
from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    """
    form for taking tasks from user for Todo app
    """
    title = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "Add new task..."})
    )

    class Meta:
        model = Task
        fields = ("title", "completed",)
