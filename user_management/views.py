from django.shortcuts import render
from django.views.generic import ListView
from .models import Role

class RolesViewList(ListView):
    model = Role
    template_name = 'roles_list.html'
    context_object_name = 'roles'
