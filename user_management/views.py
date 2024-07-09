from django.shortcuts import render
from django.views.generic import ListView, CreateView
from django.contrib.auth.forms import UserCreationForm
from .models import Role, User
from django.urls import reverse_lazy
from .forms import SignUpForm

class UsersListView(ListView):
    model = User
    template_name = 'users_list.html'
    context_object_name = 'users'
    
class RolesListView(ListView):
    model = Role
    template_name = 'roles_list.html'
    context_object_name = 'roles'

class UserRegisterView(CreateView):
    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')


