from django_tables2 import tables, CheckBoxColumn

from .models import *


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
