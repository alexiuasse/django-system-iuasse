from django.shortcuts import get_object_or_404, render
from django_tables2 import LazyPaginator
from django_tables2 import RequestConfig
from django_tables2.export.export import TableExport
from django.utils.translation import gettext as _
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import Permission
from app.base_views import MyPermissionMixin
from service.utils import webservice_dashboard_progressbars_ctx, domain_dashboard_ctx
from client.utils import client_dashboard_ctx
from financial.utils import financial_dashboard_ctx

from .forms import *
from .models import *
from .utils import *


class DashboardView(LoginRequiredMixin, MyPermissionMixin, View):
    model = DashboardSettings
    form_class = DashboardSettingsForm
    form_prefix = "dashboardsettingsform"
    form = None
    template_name = "dashboard/view.html"
    object = None
    page_title = _("Dashboard")
    page_title_icon = "dashboard"
    show_modal = False

    def set_form(self):
        self.form = self.form_class(
            instance=self.get_object(),
            prefix=self.form_prefix
        )

    def get_object(self):
        if not self.object:
            self.object = get_first_or_create(self.model)
        return self.object

    def get_context_data(self, **kwargs):
        if self.form == None:
            self.set_form()

        context = {
            'page_title': self.page_title,
            'page_title_icon': self.page_title_icon,
            'form': self.form,
            'show_modal': self.show_modal,
        }

        context.update(webservice_dashboard_progressbars_ctx())
        context.update(client_dashboard_ctx())
        context.update(domain_dashboard_ctx())
        context.update(financial_dashboard_ctx())

        return context

    def get_POST_data(self):
        """
        Same as get_GET_data but with the POST data.

        Override this method to process the POST data as you wish. Here the default processing is just send the copy of the POST data.
        """
        return self.request.POST.copy()

    def form_valid(self):
        """
        Check if form is valid, if it is save it, if not set show_modal to True, so the modal with form in template will show up with the errors.
        """
        if self.form.is_valid():
            self.object = self.form.save()
        else:
            self.show_modal = True

    def update(self):
        """Update a object."""
        self.check_edit_permission()
        post_data = self.get_POST_data()
        self.form = self.form_class(
            post_data,
            instance=self.get_object(),
            prefix=self.form_prefix,
        )
        self.form_valid()
        self.set_form()
        messages.success(
            self.request,
            _("Dashboard Settings was edited successfully")
        )

    def get(self, request, *args, **kwargs):
        # Check if the user has the view permission
        self.check_view_permission()
        # set the request
        self.request = request
        return render(request, self.template_name, self.get_context_data())

    def post(self, request, *args, **kwargs):
        # set the request
        self.request = request
        # if the id is different from 0, it is an update
        if request.POST.get(self.form_prefix+"-id", "0") != "0":
            self.update()

        return render(request, self.template_name, self.get_context_data())
