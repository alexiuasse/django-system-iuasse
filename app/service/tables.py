from django_tables2 import tables, CheckBoxColumn
from django.utils.safestring import mark_safe
from django_tables2.columns.base import Column
from django.utils.translation import gettext as _

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

    @staticmethod
    def render_color(value):
        return mark_safe(f"<span class='badge' style='background-color: {value}'>{value}</span>")


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


class ContractDashboardTable(tables.Table):

    # selection = CheckBoxColumn(
    #     accessor='pk',
    #     attrs={"th__input": {"onclick": "toggle(this)"}},
    #     orderable=False,
    #     exclude_from_export=True
    # )

    reference = Column(accessor="get_reference", verbose_name=_("Reference"))
    expiration = Column(verbose_name=_("Expiration (Month)"))

    class Meta:
        model = Contract
        orderable = False
        attrs = {
            'class': 'table table-striped table-hover table-vcenter card-table'
        }
        row_attrs = {'class': 'text-muted'}
        per_page = 20

        # sequence = ('selection', '...')
        fields = ['id', 'reference', 'start_date', 'expiration', 'end_date']


class WebServiceTable(tables.Table):

    selection = CheckBoxColumn(
        accessor='pk',
        attrs={"th__input": {"onclick": "toggle(this)"}},
        orderable=False,
        exclude_from_export=True
    )

    contract = Column(verbose_name=_("Contract"), accessor="contracts")

    class Meta:
        model = WebService
        attrs = {
            'class': 'table table-striped table-hover table-vcenter card-table'
        }
        row_attrs = {'class': 'text-muted'}
        per_page = 20
        sequence = ('selection', '...')
        exclude = ['created_at', 'updated_at']
