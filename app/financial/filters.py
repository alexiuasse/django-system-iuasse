import django_filters
from .models import *


class FinancialReleaseFilter(django_filters.FilterSet):

    class Meta:
        model = FinancialRelease
        fields = ['type_of_payment', 'cost_center']
