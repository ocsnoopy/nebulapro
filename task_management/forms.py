from django import forms
from .models import Client, Industry, Project, Task

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['industry', 'name', 'email', 'phone_number', 'active', 'user']

    def __init__(self, *args, **kwargs):
        super(ClientForm, self).__init__(*args, **kwargs)

        self.fields['industry'].widget.attrs['class'] = 'form-control'
        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['phone_number'].widget.attrs['class'] = 'form-control'
        self.fields['user'].widget.attrs['class'] = 'form-control'

class IndustryForm(forms.ModelForm):
    class Meta:
        model = Industry
        fields = ['name', 'description']

    def __init__(self, *args, **kwargs):
        super(IndustryForm, self).__init__(*args, **kwargs)

        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['description'].widget.attrs['class'] = 'form-control'

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'active', 'client', 'status', 'start_date', 'end_date', 'total_costs']

    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)

        self.fields['title'].widget.attrs['class'] = 'form-control'
        self.fields['client'].widget.attrs['class'] = 'form-control'
        self.fields['status'].widget.attrs['class'] = 'form-control'
        self.fields['start_date'].widget.attrs['class'] = 'form-control'
        self.fields['end_date'].widget.attrs['class'] = 'form-control'
        self.fields['total_costs'].widget.attrs['class'] = 'form-control'

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'project', 'status', 'reporter', 'assignee', 'deadline_date', 'last_modified_date', 'last_modified_by']

    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)

        self.fields['title'].widget.attrs['class'] = 'form-control'
        self.fields['project'].widget.attrs['class'] = 'form-control'
        self.fields['status'].widget.attrs['class'] = 'form-control'
        self.fields['reporter'].widget.attrs['class'] = 'form-control'
        self.fields['assignee'].widget.attrs['class'] = 'form-control'
        self.fields['deadline_date'].widget.attrs['class'] = 'form-control'
        self.fields['last_modified_date'].widget.attrs['class'] = 'form-control'
        self.fields['last_modified_by'].widget.attrs['class'] = 'form-control'
