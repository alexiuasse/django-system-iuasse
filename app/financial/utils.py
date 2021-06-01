from django.utils.translation import gettext as _
from django.conf import settings
from django.db.models import Sum
from datetime import datetime

from .models import *


def financial_dashboard_ctx():
    """Return context data about financial"""
    current_date = datetime.today()
    asset_total = FinancialRelease.objects.filter(
        date__year=current_date.year,
        cost_center__asset=True,
    ).values('total_value').aggregate(total=Sum('total_value'))['total'] or 0
    liability_total = FinancialRelease.objects.filter(
        date__year=current_date.year,
        cost_center__liability=True,
    ).values('total_value').aggregate(total=Sum('total_value'))['total'] or 0
    total = asset_total - liability_total
    icon = 'trending_up' if total > 0 else 'trending_down'
    icon_class = 'text-success' if total > 0 else 'text-danger'
    return {
        'financial': {
            'title': _("Financial"),
            'count': "{} {}".format(settings.MONEY_SYMBOL, total),
            'icon': icon,
            'icon_class': icon_class,
        },
    }
