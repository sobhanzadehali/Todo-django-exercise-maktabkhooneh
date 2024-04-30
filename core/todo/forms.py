from django import forms
from .models import Task


class TaskUpdateForm(forms.ModelForm):
    title = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control rounded-4",
                "name": "title",
                "placeholder": "enter the title",
            }
        ),
        label="",  # when it take a value here, it will overlap
    )

    class Meta:
        model = Task
        fields = ("title",)
