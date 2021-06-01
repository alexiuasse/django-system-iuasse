from django.urls import path
from django.urls.conf import include

from .views import *

app_name = 'service'

type_of_service_patterns = ([
    path('view/', TypeOfServiceView.as_view(), name='view'),
], 'typeofservice')

domain_patterns = ([
    path('view/', DomainView.as_view(), name='view'),
], 'domain')

contract_patterns = ([
    path('view/', ContractView.as_view(), name='view'),
], 'contract')

web_service_patterns = ([
    path('view/', WebServiceView.as_view(), name='view'),
], 'webservice')

urlpatterns = [
    path('type/service/', include(type_of_service_patterns)),
    path('domain/', include(domain_patterns)),
    path('contract/', include(contract_patterns)),
    path('web/service/', include(web_service_patterns)),
    path('dashboard/web/service/data/chart/', webservice_data_chart,
         name='webservice-data-chart'),
    path('dashboard/domain/data/chart/', domain_data_chart,
         name='domain-data-chart'),
]
