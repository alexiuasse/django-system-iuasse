from django import template
from django.conf import settings
from django.contrib.humanize.templatetags.humanize import intcomma

register = template.Library()


@register.filter
def currency(number, decimal_places=settings.DEFAULT_DECIMAL_PLACES,
             decimal=','):
    result = intcomma(number)
    result += decimal if decimal not in result else ''
    while len(result.split(decimal)[1]) != decimal_places:
        result += '0'
    return "{} {}".format(settings.MONEY_SYMBOL, result)
