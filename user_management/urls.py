from django.urls import path
from .views import RolesListView, UserRegisterView, UsersListView, AddUserView, AddRoleView, EditUserView, EditRoleView, PasswordsChangeView, password_success

urlpatterns = [
    path('roles/', RolesListView.as_view(), name='roles-list'),
    path('register/', UserRegisterView.as_view(), name = 'register'),
    path('users/', UsersListView.as_view(), name='users-list'),
    path('add_user/', AddUserView.as_view(), name='add-user'),
    path('add_role/', AddRoleView.as_view(), name='add-role'),
    path('edit_user/<int:pk>/', EditUserView.as_view(), name='edit_user'),
    path('edit_role/<int:pk>/', EditRoleView.as_view(), name='edit_role'),
    path('password/', PasswordsChangeView.as_view(template_name = 'registration/change-password.html'), name = 'change_password'),
    path('password_success', password_success, name = 'password_success'),
]


