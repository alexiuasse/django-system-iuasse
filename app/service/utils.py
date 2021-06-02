from django.utils.translation import gettext as _
from datetime import datetime

from .models import *


def webservice_dashboard_progressbars_ctx():
    """Return context data about webservice progressbars."""
    webservice_count = WebService.objects.count()
    type_of_services = {}
    for s in TypeOfService.objects.filter(active=True):
        s_count = WebService.objects.filter(type_of_service=s).count()
        type_of_services.update({
            s.name: {
                'count': s_count,
                'percentage': "{}%".format((s_count/webservice_count)*100),
                'color': s.color
            }
        })
    return {
        'webservice_progressbars': {
            'name': _("Web Service"),
            'count': webservice_count,
            'services': type_of_services,
            'icon': None,
            'icon_class': None,
        },
    }


def domain_dashboard_ctx():
    """Return context data about domain"""
    current_date = datetime.today()
    return {
        'domain': {
            'title': _("Domain"),
            'count': Domain.objects.filter(acquisition_date__year=current_date.year).values('id').count(),
            'icon': None,
            'icon_class': None,
        },
    }


def contract_dashboard_ctx():
    """Return context data about contract"""
    current_date = datetime.today()
    return {
        'contract': {
            'title': _("Contract"),
            'count': Contract.objects.filter(start_date__year=current_date.year).values('id').count(),
            'icon': None,
            'icon_class': None,
        },
    }
