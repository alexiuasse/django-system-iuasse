from django_tables2 import tables, TemplateColumn, Column

from .models import *


class ClientTable(tables.Table):

    class Meta:
        model = Client
        attrs = {'class': 'table table-striped table-hover table-vcenter card-table'}
        row_attrs = {'class': 'text-muted'}
        per_page = 20
