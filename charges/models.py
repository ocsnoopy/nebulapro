from django.db import models
from task_management.models import Client, Task, Project
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from django.urls import reverse


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

@receiver(post_save, sender=Cost)
def create_cost_approval_request(sender, instance, created, *args, **kwargs):
    if created:
        CostApprovalRequest.objects.create(
            name=f"Approval for {instance.name}",
            cost=instance,
            task=instance.task
        )

class CostApprovalRequest(models.Model):
    name = models.CharField(max_length=225)
    cost = models.ForeignKey(Cost, null = False, on_delete=models.CASCADE)
    status = models.CharField(max_length=225, choices=COST_APPROVAL_REQUEST_STATUS_CHOICES, default = 'draft')
    task = models.ForeignKey(Task, null = False, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

@receiver(post_save, sender=CostApprovalRequest)
def send_approval_request_email(sender, instance, created, *args, **kwargs):
    if created:
        client_email = instance.cost.client.email

        approval_url_relative = reverse('cost_approval_details', args=[instance.id])

        approval_url = f"{settings.SITE_DOMAIN}{approval_url_relative}"

        subject = f'Approval Request for {instance.cost.name}'
        message = render_to_string('approval_request_email.html', {
            'cost_name': instance.cost.name,
            'cost_client_name': instance.cost.client.name,
            'approval_request_name': instance.name,
            'task_name': instance.task.title,
            'approval_url': approval_url,
        })
        from_email = settings.EMAIL_HOST_USER 

        send_mail(subject, message, from_email, [client_email], html_message=message)

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









