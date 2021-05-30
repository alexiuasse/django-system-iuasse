from django.urls import path
from django.urls.conf import include

from .views import *

app_name = 'financial'

financial_release_patterns = ([
    path('view/', FinancialReleaseView.as_view(), name='view'),
], 'financialrelease')

urlpatterns = [
    path('financial/release/', include(financial_release_patterns)),
]
