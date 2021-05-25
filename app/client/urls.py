
from django.urls import path

from .views import *

app_name = 'client'

urlpatterns = [
    path('view/add/', client_view_create, name='view-add'),
]
