from django.urls import path
from .views import ClientListView, ClientProjectsListView, project_tasks, TaskDetailView, IndustriesListView

urlpatterns = [
    path('clients/', ClientListView.as_view(), name='client-list'),
    path('client/<int:pk>/projects/', ClientProjectsListView.as_view(), name='client_projects'),
    path('project/<int:project_id>/tasks/', project_tasks, name='project_tasks'),
    path('task/<int:pk>/', TaskDetailView.as_view(), name='task_detail'),
    path('industries/', IndustriesListView.as_view(), name='industries-list'),
]