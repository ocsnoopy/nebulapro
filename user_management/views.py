from django.shortcuts import render
from django.views.generic import ListView, CreateView
from django.contrib.auth.forms import UserCreationForm
from .models import Role
from django.urls import reverse_lazy

class RolesViewList(ListView):
    model = Role
    template_name = 'roles_list.html'
    context_object_name = 'roles'

class UserRegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')