from django.urls import path
from .views import ClientListView, ClientProjectsListView, project_tasks, task_detail

urlpatterns = [
    path('clients/', ClientListView.as_view(), name='client-list'),
    path('clients/<int:pk>/projects/', ClientProjectsListView.as_view(), name='client_projects'),
    path('projects/<int:project_id>/tasks/', project_tasks, name='project_tasks'),
    path('task/<int:pk>/', task_detail, name='task_detail'),
]