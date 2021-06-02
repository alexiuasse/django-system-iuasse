from django.db import models
from django.conf import settings
from django.utils.translation import gettext as _
from app.models import TimeStampMixin


class DashboardSettings(TimeStampMixin):
    contract_warning_days = models.IntegerField(
        _("Contract Warning Days"), default=7,
        help_text=_(
            "Days that should be considered to warning a contract expired"
        )
    )
    month_earn_goal = models.DecimalField(verbose_name=_("Month Earn Goal"),
                                          max_digits=settings.DEFAULT_MAX_DIGITS,
                                          decimal_places=settings.DEFAULT_DECIMAL_PLACES,
                                          default=1)
    year_earn_goal = models.DecimalField(verbose_name=_("Year Earn Goal"),
                                         max_digits=settings.DEFAULT_MAX_DIGITS,
                                         decimal_places=settings.DEFAULT_DECIMAL_PLACES,
                                         default=1)
    # warning_domain = models.BooleanField(
    #     _("Warning Domain"), default=True,
    #     help_text=_("Warning when a domain is near to expire."))
    # show_financial_stats = models.BooleanField(
    #     _("Show Financial Stats"), default=True,
    #     help_text=_("Show the financial stats: Assets x Liability.")
    # )
    # show_financial_graphs = models.BooleanField(
    #     _("Show Financial Graphs"), default=True,
    #     help_text=_(
    #         "Show graphs about the financial situation, just a resume about the current year. For more detailed info go to financial report.")
    # )

    def __str__(self) -> str:
        return "Dashboard Settings"
