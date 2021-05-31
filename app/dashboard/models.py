from django.db import models
from django.utils.translation import gettext as _
from app.models import TimeStampMixin


class DashboardSettings(TimeStampMixin):
    warning_domain = models.BooleanField(
        _("Warning Domain"), default=True,
        help_text=_("Warning when a domain is near to expire."))
    show_financial_stats = models.BooleanField(
        _("Show Financial Stats"), default=True,
        help_text=_("Show the financial stats: Assets x Liability.")
    )
    show_financial_graphs = models.BooleanField(
        _("Show Financial Graphs"), default=True,
        help_text=_(
            "Show graphs about the financial situation, just a resume about the current year. For more detailed info go to financial report.")
    )

    def __str__(self) -> str:
        return "Warning Domain: {}; Show Financial Stats: {}; Show Financial Graphs: {}".format(self.warning_domain, self.show_financial_stats, self.show_financial_graphs)
