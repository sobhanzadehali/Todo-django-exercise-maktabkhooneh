from re import S
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated

from todo.models import Task
from .serializers import TaskSerializer
from .permissions import IsOwner


class TaskViewSet(ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated, IsOwner]
    filter_backends = [DjangoFilterBackend,]
    filterset_fields = ['title', 'completed']
    
    def get_queryset(self):
        tasks = Task.objects.filter(user=self.request.user)
        return tasks