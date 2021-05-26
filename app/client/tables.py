from django_tables2 import tables, TemplateColumn, Column, CheckBoxColumn

from .models import *


class ClientTable(tables.Table):

    selection = CheckBoxColumn(accessor='pk',
                               attrs={"th__input": {"onclick": "toggle(this)"}},
                               orderable=False)

    class Meta:
        model = Client
        attrs = {
            'class': 'table table-striped table-hover table-vcenter card-table'
        }
        row_attrs = {'class': 'text-muted'}
        per_page = 20
