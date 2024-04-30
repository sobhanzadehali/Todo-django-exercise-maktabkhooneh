import requests
from rest_framework.viewsets import ModelViewSet
from django.http import JsonResponse
from django_filters.rest_framework import DjangoFilterBackend
from django.views.decorators.cache import cache_page
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated

from todo.models import Task
from .serializers import TaskSerializer
from .permissions import IsOwner


class TaskViewSet(ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated, IsOwner]
    filter_backends = [
        DjangoFilterBackend,
    ]
    filterset_fields = ["title", "completed"]

    def get_queryset(self):
        tasks = Task.objects.filter(user=self.request.user)
        return tasks

@cache_page(60*20)
def weatherView(request):
    weather_data = requests.get('https://api.openweathermap.org/data/2.5/weather?lat=35.700&lon=51.39&appid=caf1619dcd9cd26660c98eca593f0b31')
    return JsonResponse(weather_data.json())