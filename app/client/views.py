from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required
from django.views.decorators.http import require_http_methods
from django_tables2 import LazyPaginator
from django_tables2 import RequestConfig
from django_tables2.export.export import TableExport
from django.utils.translation import gettext as _
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.exceptions import PermissionDenied

from .forms import *
from .tables import ClientTable
from .filters import *
from .models import Client


class ClientView(LoginRequiredMixin, PermissionRequiredMixin, View):
    permission_required = 'client.view_client'
    form_class = ClientForm
    table_class = ClientTable
    per_page = 20
    filter_class = ClientFilter
    queryset = Client.objects.all()
    template_name = "./view.html"
    page_title = _("Client")
    page_title_icon = "user"
    export_formats = ['csv', 'xls', 'xlsx']
    show_modal = False
    # action_option = None

    def get_context_data(self):
        context = {
            'page_title': self.page_title,
            'page_title_icon': self.page_title_icon,
            'form': self.form_class,
            'filter': self.filter_class,
            'table': self.table_class,
            'export_formats': self.export_formats,
            'show_modal': self.show_modal,
            # 'action_option': self.action_option,
        }
        return context

    def set_filter(self, **kwargs):
        get = kwargs['get']
        if get and 'reset-filter' in get and get['reset-filter'] == "true":
            get = None
        # must remove "__/__/____" from birthday as it is not a valid date
        if get and 'birthday' in get and get['birthday'] == "__/__/____":
            get['birthday'] = None
        # this is necessary since the phone can be empty and if so the bellow
        # string will be sent as value, and then the filter will 'fail'
        if get and 'phone' in get and get['phone'] == "(__) _ ____-____":
            get['phone'] = ""

        self.filter_class = self.filter_class(get or None)
        if self.filter_class.queryset:
            self.queryset = self.filter_class.queryset

    def set_table(self, request, **kwargs):
        # pass a filter queryset as data of table
        self.table_class = self.table_class(self.filter_class.qs)
        RequestConfig(request, paginate={
            "per_page": request.GET.get('per_page') or self.per_page,
            "paginator_class": LazyPaginator
        }).configure(self.table_class)

    def get(self, request, *args, **kwargs):
        # sent the resquet GET data as copy to remove imutable property
        self.set_filter(get=request.GET.copy())
        self.set_table(request)

        # to export table data
        export_format = request.GET.get("_export", None)
        if TableExport.is_valid_format(export_format):
            exporter = TableExport(export_format, self.table_class)
            return exporter.response("table.{}".format(export_format))

        return render(request, self.template_name, self.get_context_data())

    def post(self, request, *args, **kwargs):
        if request.POST.get('clientform-id'):
            if request.user.has_perm('client.add_client') or request.user.has_perm('client.edit_client'):
                # sent the resquet POST data as copy to remove imutable property
                self.create_update(request, post=request.POST.copy())
            else:
                raise PermissionDenied()
        else:
            # handle selection from table
            pks = request.POST.getlist("selection")
            action = request.POST.get('actions')
            if len(pks) > 0:
                selected_objects = Client.objects.filter(pk__in=pks)
                if action == 'delete':
                    selected_objects.delete()
                    self.form_class = self.form_class(None)
                elif action == 'edit':
                    # if it is a edit so the form must contain the client info
                    self.form_class = self.form_class(
                        instance=Client.objects.get(pk=pks[0]),
                        prefix="clientform",
                        initial={'id': pks[0]}
                    )
                    self.show_modal = True
                # self.action_option = action

        self.set_filter(get=request.GET.copy())
        self.set_table(request)

        return render(request, self.template_name, self.get_context_data())

    def create_update(self, request, **kwargs):
        # copying the request.POST because it is imutable and the copy is not
        post = kwargs['post']
        # change the field clientform-birthday if it matches, this occur
        # because for some reason the data-mask is sending the value as bellow
        # and then the validation form fails because it's not a date field.
        if post and 'clientform-birthday' in post and post['clientform-birthday'] == "__/__/____":
            post['clientform-birthday'] = None
        # check if the id of client is set, if true than pass a instance
        # of client to form, as it is an update
        if post and 'clientform-id' in post and post['clientform-id'] != "0":
            if request.user.has_perm('client.edit_client'):
                self.form_class = self.form_class(
                    post,
                    instance=Client.objects.get(pk=post['clientform-id']), prefix="clientform"
                )
            else:
                raise PermissionDenied()
        else:
            # must set the prefix to get the right fields, this is
            # necessary because this view can return multiple forms
            if request.user.has_perm('client.add_client'):
                self.form_class = self.form_class(
                    post or None,
                    prefix="clientform"
                )
            else:
                raise PermissionDenied()

        if self.form_class.is_valid():
            self.form_class.save()
            self.form_class = ClientForm(None)
        else:
            self.show_modal = True
