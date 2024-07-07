from django.contrib import admin
from .models import Cost, CostApprovalRequest, Bill, PaymentRequest, Payment

admin.site.register(Cost)
admin.site.register(CostApprovalRequest)
admin.site.register(Bill)
admin.site.register(PaymentRequest)
admin.site.register(Payment)
