from django.urls import path
from .views import RolesViewList

urlpatterns = [
    path('roles/', RolesViewList.as_view(), name='roles-list'),
]