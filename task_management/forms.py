from django import forms
from .models import Client, Industry, Project, Task

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['industry', 'name', 'email', 'phone_number', 'active', 'user']

class IndustryForm(forms.ModelForm):
    class Meta:
        model = Industry
        fields = ['name', 'description']

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'active', 'client', 'status', 'start_date', 'end_date', 'total_costs']

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'project', 'status', 'reporter', 'assignee', 'deadline_date', 'last_modified_date', 'last_modified_by']