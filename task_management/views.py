from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from .models import Client, Project

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