from django.utils.translation import gettext as _
from app.base_views import MyViewCreateUpdateDelete

from .forms import *
from .tables import *
from .filters import *
from .models import *


class FinancialReleaseView(MyViewCreateUpdateDelete):
    model = FinancialRelease
    form_class = FinancialReleaseForm
    form_prefix = "financialreleaseform"
    table_class = FinancialReleaseTable
    filter_class = FinancialReleaseFilter
    queryset = FinancialRelease.objects.all()
    template_name = "financial_release/view.html"
    page_title = _("Financial Release")
    page_title_icon = "file_invoice"
    show_modal = False
