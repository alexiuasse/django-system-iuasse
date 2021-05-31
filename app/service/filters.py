import django_filters
from django import forms
from .models import *


class TypeOfServiceFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = TypeOfService
        fields = ['name', 'active']


class DomainFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    acquisition_date = django_filters.DateFilter(widget=forms.TextInput(
        attrs={"data-mask": "00/00/0000", "data-mask-visible": True, "placeholder": "00/00/0000", "autocomplete": "off"}))

    class Meta:
        model = Domain
        fields = ['name', 'acquisition_date']


class ContractFilter(django_filters.FilterSet):
    start_date = django_filters.DateFilter(widget=forms.TextInput(
        attrs={"data-mask": "00/00/0000", "data-mask-visible": True, "placeholder": "00/00/0000", "autocomplete": "off"}))

    class Meta:
        model = Contract
        fields = ['value', 'start_date', 'expiration']


class WebServiceFilter(django_filters.FilterSet):

    class Meta:
        model = WebService
        fields = ['client', 'type_of_service', 'domain']
