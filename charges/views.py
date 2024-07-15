from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DetailView
from .models import CostApprovalRequest, Cost, Bill, PaymentRequest, Payment
from .forms import CostForm, CostApprovalRequestForm, BillForm, PaymentRequestForm, PaymentForm
from django.urls import reverse_lazy

class CostApprovalRequestsView(ListView):
    model = CostApprovalRequest
    template_name = 'lists/cost_approval_requests.html'
    context_object_name = 'cost_approval_requests'

class CostsView(ListView):
    model = Cost
    template_name = 'lists/costs.html'
    context_object_name = 'costs'

class BillsView(ListView):
    model = Bill
    template_name = 'lists/bills.html'
    context_object_name = 'bills'

class PaymentRequestsView(ListView):
    model = PaymentRequest
    template_name = 'lists/payment_requests.html'
    context_object_name = 'payment_requests'

class PaymentsView(ListView):
    model = Payment
    template_name = 'lists/payments.html'
    context_object_name = 'payments'

class AddCostView(CreateView):
    model = Cost
    form_class = CostForm
    template_name = 'add_pages/add_cost.html' 
    success_url = reverse_lazy('costs-list')

class AddCostApprovalRequestView(CreateView):
    model = CostApprovalRequest
    form_class = CostApprovalRequestForm
    template_name = 'add_pages/add_cost_approval_request.html'  
    success_url = reverse_lazy('cost_approval_requests-list')

class AddBillView(CreateView):
    model = Bill
    form_class = BillForm
    template_name = 'add_pages/add_bill.html'
    success_url = reverse_lazy('bills-list')

class AddPaymentRequestView(CreateView):
    model = PaymentRequest
    form_class = PaymentRequestForm
    template_name = 'add_pages/add_payment_request.html' 
    success_url = reverse_lazy('payment-requests-list')

class AddPaymentView(CreateView):
    model = Payment
    form_class = PaymentForm
    template_name = 'add_pages/add_payment.html'
    success_url = reverse_lazy('payments-list') 


class EditCostView(UpdateView):
    model = Cost
    form_class = CostForm
    template_name = 'edit_pages/edit_cost.html'  
    success_url = reverse_lazy('costs-list')

class EditCostApprovalRequestView(UpdateView):
    model = CostApprovalRequest
    form_class = CostApprovalRequestForm
    template_name = 'edit_pages/edit_cost_approval_request.html'  
    success_url = reverse_lazy('cost-approval-requests-list')

class EditBillView(UpdateView):
    model = Bill
    form_class = BillForm
    template_name = 'edit_pages/edit_bill.html'  
    success_url = reverse_lazy('bills-list')

class EditPaymentRequestView(UpdateView):
    model = PaymentRequest
    form_class = PaymentRequestForm
    template_name = 'edit_pages/edit_payment_request.html'  
    success_url = reverse_lazy('payment-requests-list')

class EditPaymentView(UpdateView):
    model = Payment
    form_class = PaymentForm
    template_name = 'edit_pages/edit_payment.html'  
    success_url = reverse_lazy('payments-list')

class CostApprovalRequestDetailView(DetailView):
    model = CostApprovalRequest
    template_name = 'details/cost_approval_request_detail.html'
    context_object_name = "cost_approval_request"

class CostDetailView(DetailView):
    model = Cost
    template_name = 'details/cost_detail.html'

class BillDetailView(DetailView):
    model = Bill
    template_name = 'details/bill_detail.html'

class PaymentRequestDetailView(DetailView):
    model = PaymentRequest
    template_name = 'details/payment_request_detail.html'
    context_object_name = 'payment_request'

class PaymentDetailView(DetailView):
    model = Payment
    template_name = 'details/payment_detail.html'