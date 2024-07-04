from django.shortcuts import render
from django.views.generic import ListView
from .models import CostApprovalRequest, Cost

class CostApprovalRequestsView(ListView):
    model = CostApprovalRequest
    template_name = 'cost_approval_requests.html'
    context_object_name = 'cost_approval_requests'

class CostsView(ListView):
    model = Cost
    template_name = 'costs.html'
    context_object_name = 'costs'