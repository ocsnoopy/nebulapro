from django.db import models
from django.contrib.auth.models import User


class Role(models.Model):
    name = models.CharField(max_length=225)
    description = models.TextField()

class User(models.Model):
    role = models.ForeignKey(Role, null = True, on_delete=models.CASCADE)