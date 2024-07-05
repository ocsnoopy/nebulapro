from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Client, Project, Task, Industry

class ClientListView(ListView):
    model = Client
    template_name = 'clients/client_list.html'
    context_object_name = 'clients'

class ClientProjectsListView(ListView):
    model = Project
    template_name = 'clients/client_projects.html'
    context_object_name = 'projects'

    def get_queryset(self):
        client_id = self.kwargs['pk']
        client = get_object_or_404(Client, pk=client_id)
        return Project.objects.filter(client=client)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        client_id = self.kwargs['pk']
        client = get_object_or_404(Client, pk=client_id)
        context['client'] = client
        return context
    
class IndustriesListView(ListView):
    model = Industry
    template_name = 'industries_list.html'
    context_object_name = 'industries'

class TaskDetailView(DetailView):
    model = Task
    template_name = 'clients/task_detail.html'  
    context_object_name = 'task' 

def project_tasks(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    tasks = Task.objects.filter(project=project)
    
    status_data = {
        'Back Log': tasks.filter(status='back_log'),
        'In Progress': tasks.filter(status='in_progress'),
        'In Review': tasks.filter(status='in_review'),
        'Ready For Schedule': tasks.filter(status='ready_for_schedule'),
        'Scheduled': tasks.filter(status='scheduled'),
        'Done': tasks.filter(status='done'),
    }
    
    return render(request, 'clients/project_tasks.html', {
        'project': project,
        'status_data': status_data
    })
