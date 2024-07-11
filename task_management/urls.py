from django.urls import path
from .views import ClientListView, ClientProjectsListView, project_tasks, TaskDetailView, IndustriesListView, ProjectsListView, TasksListView, AddClientView, AddIndustryView, AddProjectView, AddTaskView, EditClientView, EditIndustryView, EditProjectView, EditTaskView

urlpatterns = [
    path('clients/', ClientListView.as_view(), name='client-list'),
    path('client/<int:pk>/projects/', ClientProjectsListView.as_view(), name='client_projects'),
    path('project/<int:project_id>/tasks/', project_tasks, name='project_tasks'),
    path('task/<int:pk>/', TaskDetailView.as_view(), name='task_detail'),
    path('industries/', IndustriesListView.as_view(), name='industries-list'),
    path('projects/', ProjectsListView.as_view(), name='projects-list'),
    path('tasks/', TasksListView.as_view(), name='tasks-list'),
    path('add_client/', AddClientView.as_view(), name='add-client'),
    path('add_industry/', AddIndustryView.as_view(), name='add-industry'),
    path('add_project/', AddProjectView.as_view(), name='add-project'),
    path('add_task/', AddTaskView.as_view(), name='add-task'),
    path('clients/edit/<int:pk>/', EditClientView.as_view(), name='edit_client'),
    path('industries/edit/<int:pk>/', EditIndustryView.as_view(), name='edit_industry'),
    path('projects/edit/<int:pk>/', EditProjectView.as_view(), name='edit_project'),
    path('tasks/edit/<int:pk>/', EditTaskView.as_view(), name='edit_task'),
]