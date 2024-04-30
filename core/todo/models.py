from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Task(models.Model):
    """
    this models just holds a title of task for todo app
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    completed = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        order_with_respect_to = "user"

    def get_username(self):
        return self.user.username

    def __str__(self):
        return self.title
