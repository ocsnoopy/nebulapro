from django import forms
from .models import Cost, CostApprovalRequest, Bill, PaymentRequest, Payment

class CostForm(forms.ModelForm):
    class Meta:
        model = Cost
        fields = ['name', 'amount', 'client', 'task', 'description', 'project', 'status']

class CostApprovalRequestForm(forms.ModelForm):
    class Meta:
        model = CostApprovalRequest
        fields = ['name', 'cost', 'status', 'task']

class BillForm(forms.ModelForm):
    class Meta:
        model = Bill
        fields = ['name', 'client', 'project', 'description', 'bill_registered_date', 'bill_paid_date', 'total', 'status']

class PaymentRequestForm(forms.ModelForm):
    class Meta:
        model = PaymentRequest
        fields = ['name', 'description', 'bill', 'cost', 'amount', 'status']

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['name', 'cost', 'bill', 'client', 'project', 'task', 'amount']