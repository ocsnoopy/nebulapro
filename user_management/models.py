from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse

class Role(models.Model):
    name = models.CharField(max_length=225)
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    

class User(AbstractUser):
    role = models.ForeignKey(Role, null = True, on_delete=models.SET_NULL)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username
    
    def get_absolute_url(self):
        return reverse('users-list')


