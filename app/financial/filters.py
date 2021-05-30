import django_filters
from .models import *


class PaymentStatusFilter(django_filters.FilterSet):

    class Meta:
        model = PaymentStatus
        fields = ['name', 'active']


class TypeOfPaymentFilter(django_filters.FilterSet):

    class Meta:
        model = TypeOfPayment
        fields = ['name', 'active']


class CostCenterFilter(django_filters.FilterSet):

    class Meta:
        model = CostCenter
        fields = ['name', 'asset', 'liability']


class FinancialReleaseFilter(django_filters.FilterSet):

    class Meta:
        model = FinancialRelease
        fields = ['type_of_payment', 'cost_center']
