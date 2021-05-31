from django.utils.translation import gettext as _

from .models import *


def dashboard_stats():
    return {
        'service': {
            'row_deck_top': {
                'domain': {
                    'title': _("Domains"),
                    'subtitle': Domain.objects.count(),
                    'icon': ''
                },
                'webservice': {
                    'title': _("Web Services"),
                    'subtitle': WebService.objects.count(),
                    'icon': '',
                },
                'contract': {
                    'title': _("Contracts"),
                    'subtitle': Contract.objects.count(),
                    'icon': '',
                }
            },
        }
    }
