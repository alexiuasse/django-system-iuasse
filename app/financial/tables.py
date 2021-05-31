from django_tables2 import tables, CheckBoxColumn

from .models import *


class PaymentStatusTable(tables.Table):

    selection = CheckBoxColumn(
        accessor='pk',
        attrs={"th__input": {"onclick": "toggle(this)"}},
        orderable=False,
        exclude_from_export=True
    )

    class Meta:
        model = PaymentStatus
        attrs = {
            'class': 'table table-striped table-hover table-vcenter card-table'
        }
        row_attrs = {'class': 'text-muted'}
        per_page = 20
        sequence = ('selection', '...')
        exclude = ['created_at', 'updated_at']


class TypeOfPaymentTable(tables.Table):

    selection = CheckBoxColumn(
        accessor='pk',
        attrs={"th__input": {"onclick": "toggle(this)"}},
        orderable=False,
        exclude_from_export=True
    )

    class Meta:
        model = TypeOfPayment
        attrs = {
            'class': 'table table-striped table-hover table-vcenter card-table'
        }
        row_attrs = {'class': 'text-muted'}
        per_page = 20
        sequence = ('selection', '...')
        exclude = ['created_at', 'updated_at']


class CostCenterTable(tables.Table):

    selection = CheckBoxColumn(
        accessor='pk',
        attrs={"th__input": {"onclick": "toggle(this)"}},
        orderable=False,
        exclude_from_export=True
    )

    class Meta:
        model = CostCenter
        attrs = {
            'class': 'table table-striped table-hover table-vcenter card-table'
        }
        row_attrs = {'class': 'text-muted'}
        per_page = 20
        sequence = ('selection', '...')
        exclude = ['created_at', 'updated_at']


class FinancialReleaseTable(tables.Table):

    selection = CheckBoxColumn(
        accessor='pk',
        attrs={"th__input": {"onclick": "toggle(this)"}},
        orderable=False,
        exclude_from_export=True
    )

    class Meta:
        model = FinancialRelease
        attrs = {
            'class': 'table table-striped table-hover table-vcenter card-table'
        }
        row_attrs = {'class': 'text-muted'}
        per_page = 20
        sequence = ('selection', '...')
        exclude = ['created_at', 'updated_at']
