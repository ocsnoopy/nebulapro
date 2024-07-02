from django.urls import path
from .views import ClientListView, ClientProjectsListView


urlpatterns = [
    path('clients/', ClientListView.as_view(), name='client-list'),
    path('clients/<int:pk>/projects/', ClientProjectsListView.as_view(), name='client_projects'),
]