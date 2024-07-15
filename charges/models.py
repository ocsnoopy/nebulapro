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

BILL_STATUS_CHOICES = (
    ('draft','Draft'),
    ('sent', 'Sent'),
    ('paid','Paid'),
)

PAYMENT_REQUEST_STATUS_CHOICES = (
    ('draft','Draft'),
    ('sent', 'Sent'),
    ('paid','Paid'),
)

class Cost(models.Model):
    name = models.CharField(max_length=225)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    client = models.ForeignKey(Client, null = False, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, null = False, on_delete=models.CASCADE)
    description = models.TextField()
    project = models.ForeignKey(Project, null = False, on_delete=models.CASCADE)
    status = models.CharField(max_length=225, choices=COST_STATUS_CHOICES, default = 'requested')
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class CostApprovalRequest(models.Model):
    name = models.CharField(max_length=225)
    cost = models.ForeignKey(Cost, null = False, on_delete=models.CASCADE)
    status = models.CharField(max_length=225, choices=COST_APPROVAL_REQUEST_STATUS_CHOICES, default = 'draft')
    task = models.ForeignKey(Task, null = False, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Bill(models.Model):
    name = models.CharField(max_length=225)
    client = models.ForeignKey(Client, null = False, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, null = True, on_delete=models.CASCADE)
    description = models.TextField()
    bill_registered_date = models.DateField()
    bill_paid_date = models.DateField()
    total = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=225, choices=BILL_STATUS_CHOICES, default = 'back_log')
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

class PaymentRequest(models.Model):
    name = models.CharField(max_length=225)
    description = models.TextField()
    bill = models.ForeignKey(Bill, null = False, on_delete=models.CASCADE)
    cost = models.ForeignKey(Cost, null = False, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    status = models.CharField(max_length=225, choices=PAYMENT_REQUEST_STATUS_CHOICES, default = 'back_log')
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

class Payment(models.Model):
    name = models.CharField(max_length=225)
    cost = models.ForeignKey(Cost, null = False, on_delete=models.CASCADE)
    bill = models.ForeignKey(Bill, null = False, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, null = False, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, null = True, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, null = True, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name









