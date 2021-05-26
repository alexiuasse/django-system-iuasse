
from django.urls import path

from .views import *

app_name = 'client'

urlpatterns = [
    path('view/add/', ClientView.as_view(), name='view-add'),
]
