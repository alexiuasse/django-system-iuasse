from django.utils.translation import gettext as _
from app.base_views import MyViewCreateUpdateDelete
from django.utils.timezone import now

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
