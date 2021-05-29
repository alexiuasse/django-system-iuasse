from typing import Sequence
from django_tables2 import tables, TemplateColumn, Column, CheckBoxColumn

from .models import Client, Occupation


class OccupationTable(tables.Table):

    selection = CheckBoxColumn(
        accessor='pk',
        attrs={"th__input": {"onclick": "toggle(this)"}},
        orderable=False,
        exclude_from_export=True
    )

    class Meta:
        model = Occupation
        attrs = {
            'class': 'table table-striped table-hover table-vcenter card-table'
        }
        row_attrs = {'class': 'text-muted'}
        per_page = 20
        sequence = ('selection', '...')


class ClientTable(tables.Table):

    selection = CheckBoxColumn(
        accessor='pk',
        attrs={"th__input": {"onclick": "toggle(this)"}},
        orderable=False,
        exclude_from_export=True
    )

    class Meta:
        model = Client
        attrs = {
            'class': 'table table-striped table-hover table-vcenter card-table'
        }
        row_attrs = {'class': 'text-muted'}
        per_page = 20
        # this tell that the selection will be displayed first and then '...'
        # the other fields
        sequence = ('selection', '...')
