from django.http.response import JsonResponse
from django.utils.translation import gettext as _
from django.contrib.auth.decorators import login_required, permission_required
from datetime import datetime
from django.conf import settings

from app.base_views import MyViewCreateUpdateDelete

from .forms import ClientForm, OccupationForm
from .tables import ClientTable, OccupationTable
from .filters import ClientFilter, OccupationFilter
from .models import Client, Occupation


class OccupationView(MyViewCreateUpdateDelete):
    model = Occupation
    form_class = OccupationForm
    form_prefix = "occupationform"
    table_class = OccupationTable
    filter_class = OccupationFilter
    queryset = Occupation.objects.all()
    template_name = "occupation/view.html"
    page_title = _("Occupation")
    # page_title_icon = "user"
    show_modal = False


class ClientView(MyViewCreateUpdateDelete):
    model = Client
    form_class = ClientForm
    form_prefix = "clientform"
    table_class = ClientTable
    filter_class = ClientFilter
    queryset = Client.objects.all()
    template_name = "client/view.html"
    page_title = _("Client")
    page_title_icon = "user"
    show_modal = False

    def get_POST_data(self):
        post_data = super().get_POST_data()
        if post_data.get(self.form_prefix+'-birthday', "__/__/____") == "__/__/____":
            post_data[self.form_prefix+'-birthday'] = None
        return post_data


@login_required
@permission_required('client.view_client')
def new_client_data_chart(request):
    current_date = datetime.today()
    months = [i for i in range(1, 13)]
    data = {'series': [{"name": _("Client"), "data": []}],
            'labels': settings.CHART_MONTHS_LABELS}

    client_count = []
    for month in months:
        client_count.append(Client.objects.filter(
            date__month=month,
            date__year=current_date.year
        ).values('id').count())

    data['series'][0]['data'] = client_count
    return JsonResponse(data)
