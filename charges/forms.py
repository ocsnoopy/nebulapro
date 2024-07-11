from django import forms
from .models import Cost, CostApprovalRequest, Bill, PaymentRequest, Payment

class CostForm(forms.ModelForm):
    class Meta:
        model = Cost
        fields = ['name', 'amount', 'client', 'task', 'description', 'project', 'status']

    def __init__(self, *args, **kwargs):
        super(CostForm, self).__init__(*args, **kwargs)

        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['amount'].widget.attrs['class'] = 'form-control'
        self.fields['client'].widget.attrs['class'] = 'form-control'
        self.fields['task'].widget.attrs['class'] = 'form-control'
        self.fields['description'].widget.attrs['class'] = 'form-control'
        self.fields['project'].widget.attrs['class'] = 'form-control'
        self.fields['status'].widget.attrs['class'] = 'form-control'
        
class CostApprovalRequestForm(forms.ModelForm):
    class Meta:
        model = CostApprovalRequest
        fields = ['name', 'cost', 'status', 'task']

    def __init__(self, *args, **kwargs):
        super(CostApprovalRequestForm, self).__init__(*args, **kwargs)

        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['cost'].widget.attrs['class'] = 'form-control'
        self.fields['status'].widget.attrs['class'] = 'form-control'
        self.fields['task'].widget.attrs['class'] = 'form-control'


class BillForm(forms.ModelForm):
    class Meta:
        model = Bill
        fields = ['name', 'client', 'project', 'description', 'bill_registered_date', 'bill_paid_date', 'total', 'status']

    def __init__(self, *args, **kwargs):
        super(BillForm, self).__init__(*args, **kwargs)

        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['client'].widget.attrs['class'] = 'form-control'
        self.fields['project'].widget.attrs['class'] = 'form-control'
        self.fields['description'].widget.attrs['class'] = 'form-control'
        self.fields['bill_registered_date'].widget.attrs['class'] = 'form-control'
        self.fields['bill_paid_date'].widget.attrs['class'] = 'form-control'
        self.fields['total'].widget.attrs['class'] = 'form-control'
        self.fields['status'].widget.attrs['class'] = 'form-control'

class PaymentRequestForm(forms.ModelForm):
    class Meta:
        model = PaymentRequest
        fields = ['name', 'description', 'bill', 'cost', 'amount', 'status']

    def __init__(self, *args, **kwargs):
        super(PaymentRequestForm, self).__init__(*args, **kwargs)

        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['description'].widget.attrs['class'] = 'form-control'
        self.fields['bill'].widget.attrs['class'] = 'form-control'
        self.fields['cost'].widget.attrs['class'] = 'form-control'
        self.fields['amount'].widget.attrs['class'] = 'form-control'
        self.fields['status'].widget.attrs['class'] = 'form-control'

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['name', 'cost', 'bill', 'client', 'project', 'task', 'amount']

    def __init__(self, *args, **kwargs):
        super(PaymentForm, self).__init__(*args, **kwargs)

        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['cost'].widget.attrs['class'] = 'form-control'
        self.fields['bill'].widget.attrs['class'] = 'form-control'
        self.fields['client'].widget.attrs['class'] = 'form-control'
        self.fields['project'].widget.attrs['class'] = 'form-control'
        self.fields['task'].widget.attrs['class'] = 'form-control'
        self.fields['amount'].widget.attrs['class'] = 'form-control'