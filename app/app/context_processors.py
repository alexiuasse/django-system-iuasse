from django.conf import settings  # import the settings file


def general_template_context(request):
    # return the value you want as a dictionnary. you may add multiple values in there.
    return {
        'NAME_OF_ENTERPRISE': settings.NAME_OF_ENTERPRISE,
        'NAME_OF_ENTERPRISE_SHORT': settings.NAME_OF_ENTERPRISE_SHORT,
        'CONTACT_EMAIL': settings.CONTACT_EMAIL,
        'VERSION': settings.VERSION,
        'FOOTER_LINK': settings.FOOTER_LINK,
        'FOOTER_TEXT': settings.FOOTER_TEXT,
        'FOOTER_COPYRIGHT': settings.FOOTER_COPYRIGHT,
        'DEFAULT_DECIMAL_PLACES': settings.DEFAULT_DECIMAL_PLACES,
        'DEFAULT_MAX_DIGITS': settings.DEFAULT_MAX_DIGITS,
    }
