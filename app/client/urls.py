
from django.urls import path
from django.urls.conf import include

from .views import *

app_name = 'client'

client_patterns = ([
    path('view/', ClientView.as_view(), name='view'),
], 'client')

occupation_patterns = ([
    path('view/', OccupationView.as_view(), name='view'),
], 'occupation')

urlpatterns = [
    path('client/', include(client_patterns)),
    path('occupation/', include(occupation_patterns)),
]
