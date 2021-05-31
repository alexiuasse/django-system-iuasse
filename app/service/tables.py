from django_tables2 import tables, CheckBoxColumn

from .models import *


class TypeOfServiceTable(tables.Table):

    selection = CheckBoxColumn(
        accessor='pk',
        attrs={"th__input": {"onclick": "toggle(this)"}},
        orderable=False,
        exclude_from_export=True
    )

    class Meta:
        model = TypeOfService
        attrs = {
            'class': 'table table-striped table-hover table-vcenter card-table'
        }
        row_attrs = {'class': 'text-muted'}
        per_page = 20
        sequence = ('selection', '...')
        exclude = ['created_at', 'updated_at']


class DomainTable(tables.Table):

    selection = CheckBoxColumn(
        accessor='pk',
        attrs={"th__input": {"onclick": "toggle(this)"}},
        orderable=False,
        exclude_from_export=True
    )

    class Meta:
        model = Domain
        attrs = {
            'class': 'table table-striped table-hover table-vcenter card-table'
        }
        row_attrs = {'class': 'text-muted'}
        per_page = 20
        sequence = ('selection', '...')
        exclude = ['created_at', 'updated_at']


class ContractTable(tables.Table):

    selection = CheckBoxColumn(
        accessor='pk',
        attrs={"th__input": {"onclick": "toggle(this)"}},
        orderable=False,
        exclude_from_export=True
    )

    class Meta:
        model = Contract
        attrs = {
            'class': 'table table-striped table-hover table-vcenter card-table'
        }
        row_attrs = {'class': 'text-muted'}
        per_page = 20
        sequence = ('selection', '...')
        exclude = ['created_at', 'updated_at']


class WebServiceTable(tables.Table):

    selection = CheckBoxColumn(
        accessor='pk',
        attrs={"th__input": {"onclick": "toggle(this)"}},
        orderable=False,
        exclude_from_export=True
    )

    class Meta:
        model = WebService
        attrs = {
            'class': 'table table-striped table-hover table-vcenter card-table'
        }
        row_attrs = {'class': 'text-muted'}
        per_page = 20
        sequence = ('selection', '...')
        exclude = ['created_at', 'updated_at']
