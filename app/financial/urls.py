from django.urls import path
from django.urls.conf import include

from .views import *

app_name = 'financial'

financial_release_patterns = ([
    path('view/', FinancialReleaseView.as_view(), name='view'),
], 'financialrelease')

payment_status_patterns = ([
    path('view/', PaymentStatusView.as_view(), name='view'),
], 'paymentstatus')

type_of_payment_patterns = ([
    path('view/', TypeOfPaymentView.as_view(), name='view'),
], 'typeofpayment')

cost_center_patterns = ([
    path('view/', CostCenterView.as_view(), name='view'),
], 'costcenter')

urlpatterns = [
    path('financial/release/', include(financial_release_patterns)),
    path('payment/status/', include(payment_status_patterns)),
    path('type/payment/', include(type_of_payment_patterns)),
    path('cost/center/', include(cost_center_patterns)),
    path('dashboard/data/chart/', financial_data_chart),
]
