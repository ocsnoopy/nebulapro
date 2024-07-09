from django.shortcuts import render
from django.views.generic import ListView
from .models import CostApprovalRequest, Cost, Bill, PaymentRequest, Payment

class CostApprovalRequestsView(ListView):
    model = CostApprovalRequest
    template_name = 'cost_approval_requests.html'
    context_object_name = 'cost_approval_requests'

class CostsView(ListView):
    model = Cost
    template_name = 'costs.html'
    context_object_name = 'costs'

class BillsView(ListView):
    model = Bill
    template_name = 'bills.html'
    context_object_name = 'bills'

class PaymentRequestsView(ListView):
    model = PaymentRequest
    template_name = 'payment_requests.html'
    context_object_name = 'payment_requests'

class PaymentsView(ListView):
    model = Payment
    template_name = 'payments.html'
    context_object_name = 'payments'