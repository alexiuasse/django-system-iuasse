from django.db import models
from django.conf import settings
from django.utils.translation import gettext as _
from app.models import TimeStampMixin


class DashboardSettings(TimeStampMixin):
    """Dashboard settings"""
    contract_warning_days = models.IntegerField(
        _("Contract Warning Days"),
        default=7,
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

    def __str__(self) -> str:
        return "Dashboard Settings"
