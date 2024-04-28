from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views

app_name = "api-v1"

router = DefaultRouter()

router.register("task", views.TaskViewSet, basename="task")
urlpatterns = []
urlpatterns += router.urls
