from django import forms
from django.forms import widgets
import django_filters
from .models import *


class ClientFilter(django_filters.FilterSet):
    """
    Client filter with custom fields, basically all fields from Client will appear on filter.

    The fields phone, birthday, address has some custom inputs.
    phone and birthday has masks (unfortunally you have to make some 'clean up' on these fields, because if empty they will send the masks into value)
    address is a TextField and has an autosize field with overflow as break-word. 
    """

    phone = django_filters.CharFilter(widget=forms.TextInput(
        attrs={"data-mask": "(00) 0 0000-0000", "data-mask-visible": True, "placeholder": "(00) 0 0000-0000", "autocomplete": "off"}))
    birthday = django_filters.DateFilter(widget=forms.TextInput(
        attrs={"data-mask": "00/00/0000", "data-mask-visible": True, "placeholder": "00/00/0000", "autocomplete": "off"}))
    address = django_filters.CharFilter(widget=forms.Textarea(
        attrs={"rows": 1, "data-bs-toggle": "autosize", "style": "overflow: hidden; overflow-wrap: break-word; resize: none;"}))

    class Meta:
        model = Client
        fields = '__all__'
