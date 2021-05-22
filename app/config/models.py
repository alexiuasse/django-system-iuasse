from django.db import models
from django.utils.translation import gettext as _


class TypeOfPayment(models.Model):
    """
        Model to set the type of payment allowed.
    """

    name = models.CharField(verbose_name=_("Name"), max_length=128, blank=False, null=False)
    active = models.BooleanField(verbose_name=_("Active"), default=True)


class PaymentStatus(models.Model):
    """
        Model to set the payment status.
    """

    name = models.CharField(verbose_name=_("Name"), max_length=128, blank=False, null=False)
    active = models.BooleanField(verbose_name=_("Active"), default=True)


class CostCenter(models.Model):
    """
        Model to set the cost center, this is a important model for accounting.

        In creating a financial release, a cost center is needed to identify whether it is an 'asset
        or liability '(look for more information on accounting).
    """

    name = models.CharField(verbose_name=_("Name"), max_length=128, blank=False, null=False)
    asset = models.BooleanField(verbose_name=_("Asset"))
    liability = models.BooleanField(verbose_name=_("Liability"))


class Occupation(models.Model):
    """
        Model to set the Occupation, used to identify a client.
    """

    name = models.CharField(verbose_name=_("Name"), max_length=128, blank=False, null=False)
