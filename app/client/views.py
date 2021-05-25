from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required, permission_required
from django.views.decorators.http import require_http_methods
from django.views.generic.edit import CreateView
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django_tables2 import SingleTableMixin, LazyPaginator
from django_tables2 import RequestConfig
from django.utils.translation import gettext as _
from .forms import *
from .tables import ClientTable

_page_title = _("Client")
_page_title_icon = "user"


@login_required
# @staff_member_required()
@require_http_methods(["GET", "POST"])
@permission_required(['client.add_client', 'client.view_client'], raise_exception=True)
def client_view_create(request):
    """ 
    A 'view' to show Client's in a table and to create a new client using a form inside modal.
    """
    template_name = "./view.html"
    # copying the request.POST because it is imutable and the copy is not
    post = request.POST.copy()
    # change the field clientform-birthday if it matches, this occur
    # because for some reason the data-mask is sending the value as bellow
    # and then the validation form fails because it's not a date field.
    if post and post['clientform-birthday'] == "__/__/____":
        post['clientform-birthday'] = None
    form = ClientForm(post or None)
    context = {
        'page_title': _page_title,
        'page_title_icon': _page_title_icon,
        'form': form,
    }
    if request.method == "POST":
        if form.is_valid():
            form.save()
            context.update({'form': ClientForm()})
        else:
            context.update({'error': True})
    # pass a filter
    table = ClientTable(Client.objects.all())
    RequestConfig(request, paginate={
        "per_page": 20,
        "paginator_class": LazyPaginator
    }).configure(table)
    context.update({'table': table})
    return render(request, template_name=template_name, context=context)

# class ClientView(LoginRequiredMixin, PermissionRequiredMixin, SingleTableMixin, TemplateView):
#     model = Client
#     table_class = ClientTable
#     table_data = Client.objects.all()
#     paginator_class = LazyPaginator
#     template_name = "./view.html"
#     permission_required = 'client.view_client'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['page_title'] = _page_title
#         context['page_title_icon'] = _page_title_icon
#         context['form'] = ClientForm()
#         return context

# class ClientCreateView(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
#     """A view to create a new client."""
#     model = Client
#     form_class = ClientForm
#     template_name = "./form.html"
#     permission_required = "client.add_client"
#     page_title = _page_title
#     page_title_icon = _page_title_icon
