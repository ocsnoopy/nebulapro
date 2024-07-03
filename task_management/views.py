from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from .models import Client, Project, Task


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

def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'clients/task_detail.html', {'task': task})