from django.urls import path
from .views import RolesViewList, UserRegisterView

urlpatterns = [
    path('roles/', RolesViewList.as_view(), name='roles_list'),
    path('register/', UserRegisterView.as_view(), name = 'register')
]