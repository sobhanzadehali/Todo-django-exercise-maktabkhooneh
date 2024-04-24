from django.urls import include, path
from . import views


app_name = 'todo'


urlpatterns = [
    path('',views.TaskListView.as_view(), name='task-list'),
    path('create/', views.TaskCreateView.as_view(), name='task-create'),
    path('update/<int:pk>/', views.TaskUpdateView.as_view(), name='task-update'),
    path('delete/<int:pk>/', views.TaskDeleteView.as_view(), name='task-delete'),
    path('complete/<int:pk>/', views.TaskCompleteView.as_view(), name='task-complete'),
    path('apis/', include('todo.api.v1.urls')),
]
