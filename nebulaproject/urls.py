from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('nebula_app.urls')),
    path('', include('task_management.urls')),
    path('', include('charges.urls')),
    path('users/', include('django.contrib.auth.urls')),
    path('users/', include('user_management.urls')),
]
