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
    if total > 0:
        icon = 'trending_up'
        icon_class = 'text-success'
    elif total < 0:
        icon = 'trending_down'
        icon_class = 'text-danger'
    else:
        icon = 'minus'
        icon_class = 'text-yellow'
    return {
        'financial': {
            'title': _("Financial"),
            'count': None,
            'money': total,
            'icon': icon,
            'icon_class': icon_class,
        },
    }


def get_month_revenue():
    """Return current month total revenue"""
    current_date = datetime.today()
    return FinancialRelease.objects.filter(
        date__month=current_date.month,
        date__year=current_date.year,
        cost_center__asset=True,
    ).values('total_value').aggregate(total=Sum('total_value'))['total'] or 0


def get_year_revenue():
    """Return current year total revenue"""
    current_date = datetime.today()
    return FinancialRelease.objects.filter(
        date__year=current_date.year,
        cost_center__asset=True,
    ).values('total_value').aggregate(total=Sum('total_value'))['total'] or 0
