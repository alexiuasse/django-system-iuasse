from django.http.response import JsonResponse
from django.utils.translation import gettext as _
from django.utils.timezone import now
from django.db.models import Sum
from django.contrib.auth.decorators import login_required, permission_required

from app.base_views import MyViewCreateUpdateDelete

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


@login_required
@permission_required('client.view_client')
def financial_data_chart(request):
    """
    Return a JsonResponse with data to fullfill a chart.
    The return data consists in a series with all financial divided by asset and liability for the current year (divided by month).
    If a month has nothing, so it will be sent 0.
    """
    current_date = datetime.today()
    months = [i for i in range(1, 13)]
    data = {
        'series': [],
        'labels': settings.CHART_MONTHS_LABELS,
        'colors': ['#0CC309', '#FF0000'],
    }

    assets = []
    liabilitys = []
    for month in months:
        assets.append(FinancialRelease.objects.filter(
            date__month=month,
            date__year=current_date.year,
            cost_center__asset=True,
        ).values('total_value').aggregate(total=Sum('total_value'))['total'] or 0)
        liabilitys.append(FinancialRelease.objects.filter(
            date__month=month,
            date__year=current_date.year,
            cost_center__liability=True,
        ).values('total_value').aggregate(total=Sum('total_value'))['total'] or 0)

    data['series'].append({"name": _("Asset"), "data": assets})
    data['series'].append({"name": _("Liablitity"), "data": liabilitys})
    return JsonResponse(data)
