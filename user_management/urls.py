from django.urls import path
from .views import RolesListView, UserRegisterView, UsersListView

urlpatterns = [
    path('roles/', RolesListView.as_view(), name='roles-list'),
    path('register/', UserRegisterView.as_view(), name = 'register'),
    path('users/', UsersListView.as_view(), name='users-list'),
]