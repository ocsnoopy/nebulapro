from django.contrib.auth.models import AbstractUser
from django.db import models


class Role(models.Model):
    name = models.CharField(max_length=225)
    description = models.TextField()

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Role'

class User(AbstractUser):
    role = models.ForeignKey(Role, null = True, on_delete=models.CASCADE)

