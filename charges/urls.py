from django.urls import path
from .views import CostApprovalRequestsView, CostsView, BillsView, PaymentRequestsView, PaymentsView, AddCostView, AddCostApprovalRequestView, AddBillView, AddPaymentRequestView, AddPaymentView, EditCostView, EditCostApprovalRequestView, EditBillView, EditPaymentRequestView, EditPaymentView

urlpatterns = [
    path('cost-approval-requests/', CostApprovalRequestsView.as_view(), name='cost-approval-requests-list'),
    path('costs/', CostsView.as_view(), name='costs-list'),
    path('bills/', BillsView.as_view(), name='bills-list'),
    path('payment-requests/', PaymentRequestsView.as_view(), name='payment-requests-list'),
    path('payments/', PaymentsView.as_view(), name='payments-list'),
    path('costs/add/', AddCostView.as_view(), name='add_cost'),
    path('cost_approval_requests/add/', AddCostApprovalRequestView.as_view(), name='add_cost_approval_request'),
    path('bills/add/', AddBillView.as_view(), name='add_bill'),
    path('payment-requests/add/', AddPaymentRequestView.as_view(), name='add_payment_request'),
    path('payments/add/', AddPaymentView.as_view(), name='add_payment'),
    path('costs/<int:pk>/edit/', EditCostView.as_view(), name='edit_cost'),
    path('cost-approval-requests/<int:pk>/edit/', EditCostApprovalRequestView.as_view(), name='edit_cost_approval_request'),
    path('bills/<int:pk>/edit/', EditBillView.as_view(), name='edit_bill'),
    path('payment-requests/<int:pk>/edit/', EditPaymentRequestView.as_view(), name='edit_payment_request'),
    path('payments/<int:pk>/edit/', EditPaymentView.as_view(), name='edit_payment'),
]

