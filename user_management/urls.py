from django.urls import path
from .views import RolesListView, UserRegisterView, UsersListView, AddUserView, AddRoleView, EditUserView, EditRoleView

urlpatterns = [
    path('roles/', RolesListView.as_view(), name='roles-list'),
    path('register/', UserRegisterView.as_view(), name = 'register'),
    path('users/', UsersListView.as_view(), name='users-list'),
    path('add_user/', AddUserView.as_view(), name='add-user'),
    path('add_role/', AddRoleView.as_view(), name='add-role'),
    path('edit_user/<int:pk>/', EditUserView.as_view(), name='edit_user'),
    path('edit_role/<int:pk>/', EditRoleView.as_view(), name='edit_role'),
]