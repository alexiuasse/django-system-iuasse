from django.db import models
from django.utils.translation import gettext as _
from django.conf import settings
from base.models import BaseModel


class FinancialRelease(BaseModel):
    """
        Model for financial release.
    """

    total_value = models.DecimalField(verbose_name=_("Total Value"),
                                      max_digits=settings.DEFAULT_MAX_DIGITS,
                                      decimal_places=settings.DEFAULT_DECIMAL_PLACES, help_text=_("If the type of payment is parceled out, this is the real total!"))
    type_of_payment = models.ForeignKey("config.TypeOfPayment",
                                        on_delete=models.SET_NULL,
                                        null=True,
                                        verbose_name=_("Type of Payment"), help_text="If the type of payment is parceled out, you must provide the amount of parcels. The parcels will be created automatically!")
    # must show only if type of payment is parceled out
    total_parcels = models.IntegerField(verbose_name=_("Total Parcels"),
                                        default=1)
    cost_center = models.ForeignKey("config.CostCenter",
                                    on_delete=models.SET_NULL,
                                    null=True,
                                    verbose_name=_("Cost Center"))
