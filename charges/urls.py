from django.urls import path
from .views import CostApprovalRequestsView, CostsView

urlpatterns = [
    path('cost-approval-requests/', CostApprovalRequestsView.as_view(), name='cost-approval-requests'),
    path('costs/', CostsView.as_view(), name='costs'),
]