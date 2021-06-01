from django.http.response import JsonResponse
from django.db.models import Count
from django.utils.translation import gettext as _
from django.contrib.auth.decorators import login_required, permission_required
from datetime import datetime
from dateutil.relativedelta import relativedelta

from app.base_views import MyViewCreateUpdateDelete

from .forms import *
from .tables import *
from .filters import *
from .models import *


class TypeOfServiceView(MyViewCreateUpdateDelete):
    model = TypeOfService
    form_class = TypeOfServiceForm
    form_prefix = "typeofserviceform"
    table_class = TypeOfServiceTable
    filter_class = TypeOfServiceFilter
    queryset = TypeOfService.objects.all()
    template_name = "type_of_service/view.html"
    page_title = _("Type Of Service")
    page_title_icon = "file_invoice"
    show_modal = False


class DomainView(MyViewCreateUpdateDelete):
    model = Domain
    form_class = DomainForm
    form_prefix = "domainform"
    table_class = DomainTable
    filter_class = DomainFilter
    queryset = Domain.objects.all()
    template_name = "domain/view.html"
    page_title = _("Domain")
    page_title_icon = "file_invoice"
    show_modal = False

    def get_GET_data(self):
        get_data = super().get_GET_data()
        if get_data.get('acquisition_date') == "__/__/____":
            get_data['acquisition_date'] = None
        return get_data

    def get_POST_data(self):
        post_data = super().get_POST_data()
        if post_data.get(self.form_prefix+'-acquisition_date', "__/__/____") == "__/__/____":
            post_data[self.form_prefix+'-acquisition_date'] = None
        return post_data


class ContractView(MyViewCreateUpdateDelete):
    model = Contract
    form_class = ContractForm
    form_prefix = "contractform"
    table_class = ContractTable
    filter_class = ContractFilter
    queryset = Contract.objects.all()
    template_name = "contract/view.html"
    page_title = _("Contract")
    page_title_icon = "file_invoice"
    show_modal = False

    def get_GET_data(self):
        get_data = super().get_GET_data()
        if get_data.get('start_date') == "__/__/____":
            get_data['start_date'] = None
        return get_data

    def get_POST_data(self):
        post_data = super().get_POST_data()
        if post_data.get(self.form_prefix+'-start_date', "__/__/____") == "__/__/____":
            post_data[self.form_prefix+'-start_date'] = None
        return post_data


class WebServiceView(MyViewCreateUpdateDelete):
    model = WebService
    form_class = WebServiceForm
    form_prefix = "webserviceform"
    table_class = WebServiceTable
    filter_class = WebServiceFilter
    queryset = WebService.objects.all()
    template_name = "webservice/view.html"
    page_title = _("Web Service")
    page_title_icon = "file_invoice"
    show_modal = False


@login_required
@permission_required('service.view_webservice')
def webservice_data_chart(request):
    """
    Return a JsonResponse with data to fullfill a chart.
    The return data consists in a series with all webservice divided by the type of service of the current year (divided by month).
    If a month has nothing, so it will be sent 0.

    Example:
        "series": [
            {
                "name": "type_of_service_name",
                "data": [9,9,9,9,9,9,0,0,0,0,0,0] # 12 months of data
            },
            {
                "name": "type_of_service_name",
                "data": [9,9,9,9,9,9,0,0,0,0,0,0] # 12 months of data
            }
        ],
        "labels": ["Jan", "Feb", "March",]
    """
    current_date = datetime.today()
    active_type_of_services = TypeOfService.objects.filter(active=True)
    months = [i for i in range(1, 13)]
    data = {
        'series': [],
        'labels': settings.CHART_MONTHS_LABELS,
        'colors': [type_service.color for type_service in active_type_of_services]
    }

    for type_service in active_type_of_services:
        services_count = []
        for month in months:
            services_count.append(
                WebService.objects.filter(
                    date__month=month,
                    date__year=current_date.year,
                    type_of_service=type_service
                ).values('id').count()
            )
        data['series'].append({
            "name": type_service.name,
            "data": services_count,
        })

    return JsonResponse(data)


@login_required
@permission_required('service.view_domain')
def domain_data_chart(request):
    """
    Return a JsonResponse with data to fullfill a chart.
    The return data consists in a series with all domain divided by the type of service of the current year (divided by month).
    If a month has nothing, so it will be sent 0.
    """
    current_date = datetime.today()
    months = [i for i in range(1, 13)]
    data = {
        'series': [],
        'labels': settings.CHART_MONTHS_LABELS,
    }

    domain_count = []
    for month in months:
        domain_count.append(
            Domain.objects.filter(
                acquisition_date__month=month,
                acquisition_date__year=current_date.year,
            ).values('id').count()
        )
    data['series'].append({
        "name": _("Domain"),
        "data": domain_count,
    })

    return JsonResponse(data)
