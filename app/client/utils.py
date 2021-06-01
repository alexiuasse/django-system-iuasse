from django.utils.translation import gettext as _
from datetime import datetime

from .models import *


def client_dashboard_ctx():
    """Return context data about client"""
    current_date = datetime.today()
    return {
        'client': {
            'title': _("Clients"),
            'count': Client.objects.filter(date__year=current_date.year).values('id').count(),
            'icon': None,
            'icon_class': None,
        },
    }
