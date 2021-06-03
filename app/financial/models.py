from django.db import models
from django.utils.translation import gettext as _
from django.conf import settings
from django.urls import reverse_lazy
from datetime import datetime
from django.utils.timezone import now
from app.models import TimeStampMixin


class PaymentStatus(TimeStampMixin):
    """ Model to set the payment status."""

    name = models.CharField(verbose_name=_("Name"),
                            max_length=128,
                            blank=False,
                            null=False)
    active = models.BooleanField(verbose_name=_("Active"),
                                 default=True)

    def __str__(self) -> str:
        return self.name


class TypeOfPayment(TimeStampMixin):
    """Model to set the type of payment allowed."""

    name = models.CharField(verbose_name=_("Name"),
                            max_length=128,
                            blank=False,
                            null=False)
    active = models.BooleanField(verbose_name=_("Active"),
                                 default=True)

    def __str__(self) -> str:
        return self.name


class CostCenter(TimeStampMixin):
    """
        Model to set the cost center, this is a important model for accounting.

        In creating a financial release, a cost center is needed to identify whether it is an 'asset
        or liability '(look for more information on accounting).
    """

    name = models.CharField(verbose_name=_("Name"),
                            max_length=128,
                            blank=False,
                            null=False)
    asset = models.BooleanField(verbose_name=_("Asset"))
    liability = models.BooleanField(verbose_name=_("Liability"))

    def __str__(self) -> str:
        return self.name


class FinancialRelease(TimeStampMixin):
    """Model for financial release."""

    total_value = models.DecimalField(verbose_name=_("Total Value"),
                                      max_digits=settings.DEFAULT_MAX_DIGITS,
                                      decimal_places=settings.DEFAULT_DECIMAL_PLACES, help_text=_("If the type of payment is parceled out, this is the real total!"))
    type_of_payment = models.ForeignKey("financial.TypeOfPayment",
                                        on_delete=models.SET_NULL,
                                        null=True,
                                        verbose_name=_("Type of Payment"), help_text="If the type of payment is parceled out, you must provide the amount of parcels. The parcels will be created automatically!")
    # must show only if type of payment is parceled out
    total_parcels = models.IntegerField(verbose_name=_("Total Parcels"),
                                        default=1)
    cost_center = models.ForeignKey("financial.CostCenter",
                                    on_delete=models.SET_NULL,
                                    null=True,
                                    verbose_name=_("Cost Center"))
    date = models.DateField(verbose_name=_("Date"),
                            default=now)
    attachment = models.FileField(verbose_name=_("Attachment"),
                                  upload_to="financial_release",
                                  blank=True,
                                  null=True)

    def __str__(self) -> str:
        return "{} - {}".format(self.total_value, self.type_of_payment)

    def get_absolute_url(self):
        return reverse_lazy(f'{self._meta.app_label}:{self._meta.model_name}:details')

    @staticmethod
    def get_exclude_fields():
        """
            Fields of the current model that is marked to get excluded from visualization.
        """

        return []

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
