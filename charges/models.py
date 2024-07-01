from django.db import models
from task_management.models import Client, Task, Project

COST_STATUS_CHOICES = (
    ('requested','Requested'),
    ('pending_approval', 'Pending Approval'),
    ('approved','Approved'),
    ('rejected','Rejected'),
    ('paid', 'Paid'),
)

COST_APPROVAL_REQUEST_STATUS_CHOICES = (
    ('draft','Draft'),
    ('sent', 'Sent'),
    ('accepted','Accepted'),
    ('rejected','Rejected'),
)


class Cost(models.Model):
    name = models.CharField(max_length=225)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    client = models.ForeignKey(Client, null = False, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, null = False, on_delete=models.CASCADE)
    description = models.TextField()
    project = models.ForeignKey(Project, null = False, on_delete=models.CASCADE)
    status = models.CharField(max_length=225, choices=COST_STATUS_CHOICES, default = 'requested')

    def __str__(self):
        return self.name

class CostApprovalRequest(models.Model):
    name = models.CharField(max_length=225)
    cost = models.ForeignKey(Cost, null = False, on_delete=models.CASCADE)
    status = models.CharField(max_length=225, choices=COST_APPROVAL_REQUEST_STATUS_CHOICES, default = 'draft')
    task = models.ForeignKey(Task, null = False, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Payment(models.Model):
    pass
