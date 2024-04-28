from django.test import TestCase
from rest_framework.test import APIClient
import pytest

from django.urls import reverse
from todo.models import Task

from django.contrib.auth.models import User

# Create your tests here.


@pytest.fixture
def create_user():
    user = User.objects.create_user(
        "admin", "admin@admin.com", "a/@123123", is_active=True, is_superuser=True
    )
    return user


@pytest.mark.django_db
class TestTask:
    client = APIClient()

    def test_task_model(self, create_user):
        """
        create
        """
        user = create_user
        task = Task.objects.create(user=user, title="pytest title", completed=False)

        assert task.user.email == user.email
        assert task.title == "pytest title"
        assert task.completed == False
        task.completed = True
        task.save()
        assert task.completed == True

    def test_task_list_api_not_logedin(self):
        """task list api without login"""
        url = reverse("todo:api-v1:task-list")
        response = self.client.get(url)
        assert response.status_code == 403

    def test_task_list_api_logedin(self, create_user):
        """tests task list api with loged in user

        Args:
            create_user (pytest fixture): creates a user
        """
        user = create_user
        self.client.force_authenticate(user)
        url = reverse("todo:api-v1:task-list")
        response = self.client.get(url)
        assert response.status_code == 200

    def test_task_update(self, create_user):
        """
        to update task completed  status and title with user loged in
        """
        user = create_user
        task = Task.objects.create(user=user, title="pytest title", completed=False)
        self.client.force_authenticate(user)
        url = reverse("todo:api-v1:task-detail", kwargs={"pk": task.id})
        data = {"title": "edited pytest title", "completed": True}
        response = self.client.patch(path=url, data=data)
        assert response.status_code == 200

    def test_task_delete(self, create_user):
        """tests api task delete functionality with user `loged in`"""
        user = create_user
        task = Task.objects.create(user=user, title="pytest title", completed=False)
        self.client.force_authenticate(user)
        url = reverse("todo:api-v1:task-detail", kwargs={"pk": task.id})
        response = self.client.delete(url)

        assert response.status_code == 204

    def test_task_delete_logedout(self, create_user):
        """tests api task delete functionality with user `not loged in`"""
        user = create_user
        task = Task.objects.create(user=user, title="pytest title", completed=False)
        self.client.logout()
        url = reverse("todo:api-v1:task-detail", kwargs={"pk": task.id})
        response = self.client.delete(url)

        assert response.status_code == 403
