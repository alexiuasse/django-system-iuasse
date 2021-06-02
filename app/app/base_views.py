from django.shortcuts import get_object_or_404, render
from django_tables2 import LazyPaginator
from django_tables2 import RequestConfig
from django_tables2.export.export import TableExport
from django.utils.translation import gettext as _
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied, ImproperlyConfigured
from django.contrib import messages
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import Permission


class MyPermissionMixin():

    def get_permissions(self):
        """
        Get all the permissions that the user has of a given model.
        If user is super user the return will have all permissions.

        The permissions available are ['view', 'add', 'change', 'delete']
        """
        if self.request == None:
            raise ImproperlyConfigured(
                '{0} is missing the request attribute.'.format(
                    self.__class__.__name__)
            )

        if self.request.user.is_superuser:
            return ['view', 'add', 'change', 'delete']

        permissions = Permission.objects.filter(
            content_type=ContentType.objects.get_for_model(self.model),
            user=self.request.user
        )
        return [perm.codename.split('_')[0] for perm in permissions]

    def check_view_permission(self):
        """Check for permission to view"""
        if not any('view' in item for item in self.get_permissions()):
            raise PermissionDenied()

    def check_add_permission(self):
        """Check for permission to add"""
        if not any('add' in item for item in self.get_permissions()):
            raise PermissionDenied()

    def check_edit_permission(self):
        """Check for permission to change"""
        if not any('change' in item for item in self.get_permissions()):
            raise PermissionDenied()

    def check_delete_permission(self):
        """Check for permission to delete"""
        if not any('delete' in item for item in self.get_permissions()):
            raise PermissionDenied()


class MyViewCreateUpdateDelete(LoginRequiredMixin, MyPermissionMixin, View):
    """
    This is a custom view that can view, add, edit and delete a model.
    """

    model = None
    form = None
    form_class = None
    form_prefix = None
    table_class = None
    filter_class = None
    queryset = None
    template_name = None
    page_title = None
    page_title_icon = None
    request = None
    object = None
    per_page = 20
    show_modal = False
    table_name = "table"
    export_formats = ['csv', 'xls', 'xlsx']

    def get_context_data(self):
        if self.template_name == None:
            raise ImproperlyConfigured(
                '{0} is missing the template_name attribute.'.format(
                    self.__class__.__name__)
            )
        if self.form_class == None:
            raise ImproperlyConfigured(
                '{0} is missing the form_class attribute.'.format(
                    self.__class__.__name__)
            )
        if self.form_prefix == None:
            raise ImproperlyConfigured(
                '{0} is missing the form_prefix attribute.'.format(
                    self.__class__.__name__)
            )
        if self.filter_class == None:
            raise ImproperlyConfigured(
                '{0} is missing the filter_class attribute.'.format(
                    self.__class__.__name__)
            )
        if self.table_class == None:
            raise ImproperlyConfigured(
                '{0} is missing the table_class attribute.'.format(
                    self.__class__.__name__)
            )

        # if self.form == None:
        #     self.reset_form()

        context = {
            'page_title': self.page_title,
            'page_title_icon': self.page_title_icon,
            'form': self.form,
            'filter': self.filter_class,
            'table': self.table_class,
            'export_formats': self.export_formats,
            'show_modal': self.show_modal,
        }
        return context

    def get_GET_data(self):
        """
        Return the copy of GET data, sometimes it is needed to change the data from a request, but the data from a request is imutable (for security reasons), the copy of the data is not imutable.

        Override this method to process the GET data as you wish, the default processing is to check the reset-filter, if True reset the filter data (returning None).

        This view only has GET data because of the filter, so it is ok to do this things, but if you have others things that is sent by GET (for example the size of the table) you MUST find a way yo keep those data.
        """
        if self.request.GET.get('reset-filter', False):
            return None
        return self.request.GET.copy()

    def get_POST_data(self):
        """
        Same as get_GET_data but with the POST data.

        Override this method to process the POST data as you wish. Here the default processing is just send the copy of the POST data.
        """
        return self.request.POST.copy()

    def set_form(self):
        """Set the form with instance and prefix."""
        self.form = self.form_class(
            instance=self.object,
            prefix=self.form_prefix
        )

    def reset_form(self):
        """Reset the form passing None and prefix."""
        self.form = self.form_class(
            None,
            prefix=self.form_prefix
        )

    def set_filter(self):
        """Set the filter"""
        get = self.get_GET_data()
        self.filter_class = self.filter_class(get or None)
        if self.filter_class.queryset:
            self.queryset = self.filter_class.queryset

    def set_table(self):
        """Set the table with the queryset from filter"""
        self.set_filter()
        # pass a filter queryset as data of table
        self.table_class = self.table_class(self.filter_class.qs)
        RequestConfig(self.request, paginate={
            "per_page": self.request.GET.get('per_page') or self.per_page,
            "paginator_class": LazyPaginator
        }).configure(self.table_class)

    def export_table(self, export_format):
        """Export the data table with given format."""
        exporter = TableExport(export_format, self.table_class)
        return exporter.response("{}.{}".format(self.table_name, export_format))

    def form_valid(self):
        """
        Check if form is valid, if it is save it, if not set show_modal to True, so the modal with form in template will show up with the errors.
        """
        if self.form.is_valid():
            self.object = self.form.save()
        else:
            print(self.form.errors)
            self.show_modal = True

    def create(self):
        """Create a new object."""
        self.check_add_permission()
        self.form = self.form_class(
            self.get_POST_data(),
            prefix=self.form_prefix
        )
        self.form_valid()
        self.reset_form()
        messages.success(
            self.request,
            _("{} was created successfully").format(self.object)
        )

    def update(self):
        """Update a object."""
        self.check_edit_permission()
        post_data = self.get_POST_data()
        self.form = self.form_class(
            post_data,
            instance=get_object_or_404(
                self.model, pk=post_data.get(self.form_prefix+"-id")
            ),
            prefix=self.form_prefix,
        )
        self.form_valid()
        self.reset_form()
        messages.success(
            self.request,
            _("{} was edited successfully").format(self.object)
        )

    def delete(self, pks):
        """Delete a object or a list of objects."""
        self.check_delete_permission()
        selected_objects = self.model.objects.filter(pk__in=pks)
        selected_objects.delete()
        messages.success(
            self.request,
            _("{} Client(s) deleted successfully").format(len(pks))
        )

    def get(self, request, *args, **kwargs):
        # Check if the user has the view permission
        self.check_view_permission()
        # set the request
        self.request = request
        # set the table with the filter
        self.set_table()
        # check if user request a export table if so then export
        export_format = request.GET.get("_export", None)
        if TableExport.is_valid_format(export_format):
            return self.export_table(export_format)
        # check if form is None, if so set it
        if self.form == None:
            self.set_form()
        return render(request, self.template_name, self.get_context_data())

    def post(self, request, *args, **kwargs):
        # set the request
        self.request = request
        # if the id is different from 0, it is an update
        if request.POST.get(self.form_prefix+"-id", "0") != "0":
            self.update()
        else:
            # get the selected pk models
            pks = request.POST.getlist("selection")
            # get the action, can be delete or edit
            action = request.POST.get('actions')
            if len(pks) > 0:
                if action == 'delete':
                    self.delete(pks)
                elif action == 'edit':
                    self.object = get_object_or_404(self.model, pk=pks[0])
                    # if it is a edit so the form must contain the client info
                    self.form = self.form_class(
                        instance=self.object,
                        prefix=self.form_prefix,
                        initial={'id': self.object.id}
                    )
                    self.show_modal = True
            else:
                self.create()

        self.set_table()

        return render(request, self.template_name, self.get_context_data())
