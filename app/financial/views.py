from django.utils.translation import gettext as _
from app.base_views import MyViewCreateUpdateDelete
from django.utils.timezone import now

from .forms import *
from .tables import *
from .filters import *
from .models import *


class PaymentStatusView(MyViewCreateUpdateDelete):
    model = PaymentStatus
    form_class = PaymentStatusForm
    form_prefix = "paymentstatusform"
    table_class = PaymentStatusTable
    filter_class = PaymentStatusFilter
    queryset = PaymentStatus.objects.all()
    template_name = "payment_status/view.html"
    page_title = _("Payment Status")
    page_title_icon = "file_invoice"
    show_modal = False


class TypeOfPaymentView(MyViewCreateUpdateDelete):
    model = TypeOfPayment
    form_class = TypeOfPaymentForm
    form_prefix = "typeofpaymentform"
    table_class = TypeOfPaymentTable
    filter_class = TypeOfPaymentFilter
    queryset = TypeOfPayment.objects.all()
    template_name = "type_of_payment/view.html"
    page_title = _("Type Of Payment")
    page_title_icon = "file_invoice"
    show_modal = False


class CostCenterView(MyViewCreateUpdateDelete):
    model = CostCenter
    form_class = CostCenterForm
    form_prefix = "costcenterform"
    table_class = CostCenterTable
    filter_class = CostCenterFilter
    queryset = CostCenter.objects.all()
    template_name = "cost_center/view.html"
    page_title = _("Cost Center")
    page_title_icon = "file_invoice"
    show_modal = False


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

    def get_POST_data(self):
        post_data = super().get_POST_data()
        if post_data.get(self.form_prefix+'-date', "__/__/____") == "__/__/____":
            post_data[self.form_prefix+'-date'] = now()
        return post_data
