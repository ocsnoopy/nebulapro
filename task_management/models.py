from django.db import models
from user_management.models import User
from datetime import datetime, date
from django.db.models.signals import pre_delete
from django.dispatch import receiver
from user_management.models import User

PROJECT_STATUS_CHOICES = (
    ('draft','Draft'),
    ('in_progress', 'In Progress'),
    ('done','Done'),
)

TASK_STATUS_CHOICES = (
    ('back_log','Back Log'),
    ('in_progress', 'In Progress'),
    ('in_review','In Review'),
    ('ready_for_schedule','Ready For Schedule'),
    ('scheduled', 'Scheduled'),
    ('done','Done'),
)


class Industry(models.Model):
    name = models.CharField(max_length=225)
    description = models.TextField()

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'industries'

class Client(models.Model):
    industry = models.ForeignKey(Industry, null = True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=225)
    email = models.EmailField(null = True, max_length= 100)
    phone_number = models.CharField(max_length= 20, null = True)
    active = models.BooleanField(default= False)
    user = models.ForeignKey(User, null = True, on_delete=models.SET_NULL)  

    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=225)
    active = models.BooleanField(default= False)
    client = models.ForeignKey(Client, null = False, on_delete=models.CASCADE)
    status = models.CharField(max_length=225, choices=PROJECT_STATUS_CHOICES, default = 'draft')
    start_date = models.DateField()
    end_date = models.DateField()
    total_costs = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.title

class Task(models.Model):
    title = models.CharField(max_length=225)
    project = models.ForeignKey(Project, null = True, on_delete=models.CASCADE)
    status = models.CharField(max_length=225, choices=TASK_STATUS_CHOICES, default = 'back_log')
    reporter = models.ForeignKey(User, related_name='reported_tasks', null = True, on_delete=models.SET_NULL)
    assignee = models.ForeignKey(User, related_name='assigned_tasks', null = True, on_delete=models.SET_NULL)
    deadline_date = models.DateField()
    last_modified_date = models.DateTimeField()
    last_modified_by = models.ForeignKey(User, related_name='modified_tasks', null = True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.title
