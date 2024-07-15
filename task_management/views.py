from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Client, Project, Task, Industry
from .forms import ClientForm, IndustryForm, ProjectForm, TaskForm
from django.urls import reverse_lazy


class ClientListView(ListView):
    model = Client
    template_name = 'lists/client_list.html'
    context_object_name = 'clients'

class ClientProjectsListView(ListView):
    model = Project
    template_name = 'lists/client_projects.html'
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
    template_name = 'lists/industries_list.html'
    context_object_name = 'industries'

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
    
    return render(request, 'lists/project_tasks.html', {
        'project': project,
        'status_data': status_data
    })

class ProjectsListView(ListView):
    model = Project
    template_name = 'lists/project_list.html'
    context_object_name = 'allprojects'

class TasksListView(ListView):
    model = Task
    template_name = 'lists/task_list.html'
    context_object_name = 'alltasks'

class AddClientView(CreateView):
    model = Client
    form_class = ClientForm
    template_name = 'add_pages/add_client.html'
    success_url = reverse_lazy('clients-list')

class AddIndustryView(CreateView):
    model = Industry
    form_class = IndustryForm
    template_name = 'add_pages/add_industry.html'
    success_url = reverse_lazy('industries-list')

class AddProjectView(CreateView):
    model = Project
    form_class = ProjectForm
    template_name = 'add_pages/add_project.html'
    success_url = reverse_lazy('projects-list')

class AddTaskView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'add_pages/add_task.html'
    success_url = reverse_lazy('tasks-list')

class EditClientView(UpdateView):
    model = Client
    form_class = ClientForm
    template_name = 'edit_pages/edit_client.html'
    success_url = reverse_lazy('client-list')

class EditIndustryView(UpdateView):
    model = Industry
    form_class = IndustryForm
    template_name = 'edit_pages/edit_industry.html'
    success_url = reverse_lazy('industries-list')

class EditProjectView(UpdateView):
    model = Project
    form_class = ProjectForm
    template_name = 'edit_pages/edit_project.html'
    success_url = reverse_lazy('projects-list')

class EditTaskView(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'edit_pages/edit_task.html'
    success_url = reverse_lazy('tasks-list')

class ClientDetailView(DetailView):
    model = Client
    template_name = 'details/client_detail.html'

class IndustryDetailView(DetailView):
    model = Industry
    template_name = 'details/industry_detail.html'

class ProjectDetailView(DetailView):
    model = Project
    template_name = 'details/project_detail.html'

class TaskDetailView(DetailView):
    model = Task
    template_name = 'details/task_detail.html'  