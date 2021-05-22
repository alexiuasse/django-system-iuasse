from django.db import models
from django.utils.translation import gettext as _
from django.conf import settings
from dateutil.relativedelta import relativedelta
from datetime import date
from base.models import BaseModel


class WebService(BaseModel):
    """
        Model to represent a web service, like build a One Page, a web system, an application for mobile with backend.
    """

    client = models.ForeignKey("client.Client",
                               on_delete=models.CASCADE,
                               verbose_name=_("Client"))
    type_of_service = models.ForeignKey("config.TypeOfService",
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


class Domain(BaseModel):
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


class Contract(BaseModel):
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
    description = models.TextField(verbose_name=_("Description"))
    attachment = models.FileField(verbose_name=_("Attachment"))

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
