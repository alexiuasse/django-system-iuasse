from django.db import models
from django.utils.translation import gettext as _
from django.conf import settings
from dateutil.relativedelta import relativedelta
from datetime import date
from django.urls import reverse_lazy


class TypeOfService(models.Model):
    """
        Model to set the type of service.
    """

    name = models.CharField(verbose_name=_("Name"),
                            max_length=128,
                            blank=False,
                            null=False)
    active = models.BooleanField(verbose_name=_("Active"),
                                 default=True)

    def __str__(self) -> str:
        return "{}".format(self.name)


class WebService(models.Model):
    """
        Model to represent a web service, like build a One Page, a web system, an application for mobile with backend.
    """

    client = models.ForeignKey("client.Client",
                               on_delete=models.CASCADE,
                               verbose_name=_("Client"))
    type_of_service = models.ForeignKey("service.TypeOfService",
                                        on_delete=models.SET_NULL,
                                        null=True,
                                        verbose_name=_("Type of Service"))
    domain = models.ForeignKey("service.Domain",
                               on_delete=models.SET_NULL,
                               null=True,
                               verbose_name=_("Domain"))
    # The contract is ManyToManyField because the same service can have
    # multiple contracts over time, this occurs for example when a contract has
    # expired and then a new one is contracted.
    contract = models.ManyToManyField("service.Contract",
                                      blank=True,
                                      verbose_name=_("Contract"))

    def __str__(self) -> str:
        return "{} - {}".format(self.client, self.type_of_service)

    def get_absolute_url(self):
        return reverse_lazy(f'{self._meta.app_label}:{self._meta.model_name}:view')

    def get_change_url(self):
        return reverse_lazy(f'{self._meta.app_label}:{self._meta.model_name}:change', kwargs={'pk': self.pk})

    def get_delete_url(self):
        return reverse_lazy(f'{self._meta.app_label}:{self._meta.model_name}:delete', kwargs={'pk': self.pk})

    @staticmethod
    def get_exclude_fields():
        """
            Fields of the current model that is marked to get excluded from visualization.
        """

        return ['id', 'history']

    def get_add_fields(self):
        """
            Custom fields to be added for visualization. Need to be a dict with {'name': content}
        """

        return {}

    def get_dict_data(self):
        """
            This method automatically gathers all the fields in the current model and returns them as a dictionary, used mainly to build a layout.
        """

        exclude = self.get_exclude_fields()
        data = dict([(field.verbose_name, getattr(self, field.name))
                    for field in self._meta.fields if field.name not in exclude])
        data.update(self.get_add_fields())
        return data


class Domain(models.Model):
    """
        Model to identify a domain (network domain).
    """

    name = models.CharField(verbose_name=_("Name"),
                            max_length=128)
    link = models.TextField(verbose_name=_("Link"))
    acquisition_date = models.DateField(verbose_name=_("Acquisition Date"),
                                        help_text=_("Date that the domain was buyed."))
    # The contract is ManyToManyField because the same domain can have multiple
    # contracts over time, this occurs for example when a contract has expired
    # and then a new one is contracted.
    contract = models.ManyToManyField("service.Contract",
                                      blank=True,
                                      verbose_name=_("Contract"))

    def __str__(self) -> str:
        return "{}".format(self.name)

    def get_absolute_url(self):
        return reverse_lazy(f'{self._meta.app_label}:{self._meta.model_name}:view')

    def get_change_url(self):
        return reverse_lazy(f'{self._meta.app_label}:{self._meta.model_name}:change', kwargs={'pk': self.pk})

    def get_delete_url(self):
        return reverse_lazy(f'{self._meta.app_label}:{self._meta.model_name}:delete', kwargs={'pk': self.pk})

    @staticmethod
    def get_exclude_fields():
        """
            Fields of the current model that is marked to get excluded from visualization.
        """

        return ['id', 'history']

    def get_add_fields(self):
        """
            Custom fields to be added for visualization. Need to be a dict with {'name': content}
        """

        return {}

    def get_dict_data(self):
        """
            This method automatically gathers all the fields in the current model and returns them as a dictionary, used mainly to build a layout.
        """

        exclude = self.get_exclude_fields()
        data = dict([(field.verbose_name, getattr(self, field.name))
                    for field in self._meta.fields if field.name not in exclude])
        data.update(self.get_add_fields())
        return data


class Contract(models.Model):
    """
        Model to identify a contract, this will be used in most of services.

        This model will never exist alone, it is the complement of some service.

        A contract has a value, the start date that was signed/agreed upon, an expiration in months (because most contracts have a deadline to expire and it is usually in months).

        The end date can be generated using start date and expiration (months).
    """

    value = models.DecimalField(verbose_name=_("Value"),
                                max_digits=settings.DEFAULT_MAX_DIGITS,
                                decimal_places=settings.DEFAULT_DECIMAL_PLACES)
    start_date = models.DateField(verbose_name=_("Start Date"),
                                  help_text=_("Date that the contract was signed/agreed."))
    expiration = models.IntegerField(verbose_name=_("Expiration"),
                                     default=12,
                                     help_text=_("Expiration of the contract in months."))
    description = models.TextField(verbose_name=_("Description"), blank=True)
    attachment = models.FileField(verbose_name=_("Attachment"),
                                  upload_to="contracts",
                                  blank=True,
                                  null=True)

    def __str__(self) -> str:
        return "{}/{} {} {}".format(self.start_date, self.expiration, settings.MONEY_SYMBOL, self.value)

    def expiration_date(self):
        """
            Return the expiration date using a relativedelta.
        """

        return self.start_date + relativedelta(months=self.expiration)

    def months_passed(self):
        """
            Return the months that has passed since start_date until today.
        """

        return relativedelta(self.start_date, date.today()).months

    def is_expired(self):
        """
            Check if the contract is expired. 
            (start_date + relativedelta(months=expiration)) < today
        """

        return self.expiration_date() < date.today()

    def get_absolute_url(self):
        return reverse_lazy(f'{self._meta.app_label}:{self._meta.model_name}:view')

    def get_change_url(self):
        return reverse_lazy(f'{self._meta.app_label}:{self._meta.model_name}:change', kwargs={'pk': self.pk})

    def get_delete_url(self):
        return reverse_lazy(f'{self._meta.app_label}:{self._meta.model_name}:delete', kwargs={'pk': self.pk})

    @staticmethod
    def get_exclude_fields():
        """
            Fields of the current model that is marked to get excluded from visualization.
        """

        return ['id', 'history']

    def get_add_fields(self):
        """
            Custom fields to be added for visualization. Need to be a dict with {'name': content}
        """

        return {}

    def get_dict_data(self):
        """
            This method automatically gathers all the fields in the current model and returns them as a dictionary, used mainly to build a layout.
        """

        exclude = self.get_exclude_fields()
        data = dict([(field.verbose_name, getattr(self, field.name))
                    for field in self._meta.fields if field.name not in exclude])
        data.update(self.get_add_fields())
        return data
