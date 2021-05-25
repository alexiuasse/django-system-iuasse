from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required
from django.views.decorators.http import require_http_methods
from django_tables2 import LazyPaginator
from django_tables2 import RequestConfig
from django.utils.translation import gettext as _
from .forms import *
from .tables import ClientTable
from .filters import *
from .models import Client


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
    if post and 'clientform-birthday' in post and post['clientform-birthday'] == "__/__/____":
        post['clientform-birthday'] = None
    # check if the id of client is set, if true than pass a instance of client
    # to form, as it is an update
    if post and 'clientform-id' in post and post['clientform-id'] != "0":
        form = ClientForm(
            post,
            instance=Client.objects.get(pk=post['clientform-id']), prefix="clientform"
        )
    else:
        # must set the prefix to get the right fields, this is necessary because
        # this view can return multiple forms
        form = ClientForm(post or None, prefix="clientform")

    # must remove "__/__/____" from birthday
    get = request.GET.copy()
    if get and 'birthday' in get and get['birthday'] == "__/__/____":
        get['birthday'] = None
    # this is necessary since the phone can be empty and if so the bellow
    # string will be sent as value, and then the filter will 'fail'
    if get and 'phone' in get and get['phone'] == "(__) _ ____-____":
        get['phone'] = ""
    filter = ClientFilter(get or None, queryset=Client.objects.all())

    context = {
        'page_title': _page_title,
        'page_title_icon': _page_title_icon,
        'form': form,
        'filter': filter
    }
    if request.method == "POST":
        pks = request.POST.getlist("selection")  # handle selection from table
        action = request.POST.get('action_options')
        if len(pks) > 0:
            selected_objects = Client.objects.filter(pk__in=pks)
            if action == 'delete':
                selected_objects.delete()
                context.update({'form': ClientForm(None)})
            elif action == 'edit':
                # if it is a edit so the form must contain the client info
                context.update({
                    'form': ClientForm(instance=Client.objects.get(pk=pks[0]), prefix="clientform", initial={'id': pks[0]}),
                    'showModal': True
                })
        elif 'actions' not in post:
            if form.is_valid():
                form.save()
                context.update({'form': ClientForm(None)})
            else:
                context.update({'showModal': True})
        else:
            context.update({'form': ClientForm(None)})
    # pass a filter
    table = ClientTable(filter.qs)
    RequestConfig(request, paginate={
        "per_page": 20,
        "paginator_class": LazyPaginator
    }).configure(table)
    context.update({'table': table})
    return render(request, template_name=template_name, context=context)
