from django.urls import path
from .views import CostApprovalRequestsView, CostsView, BillsView, PaymentRequestsView, PaymentsView

urlpatterns = [
    path('cost-approval-requests/', CostApprovalRequestsView.as_view(), name='cost-approval-requests'),
    path('costs/', CostsView.as_view(), name='costs'),
    path('bills/', BillsView.as_view(), name='bills'),
    path('payment-requests/', PaymentRequestsView.as_view(), name='payment-requests'),
    path('payments/', PaymentsView.as_view(), name='payments'),
]

