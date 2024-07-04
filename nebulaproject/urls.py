from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('task_management.urls')),
    path('', include('user_management.urls')),
    path('', include('charges.urls')),
]
