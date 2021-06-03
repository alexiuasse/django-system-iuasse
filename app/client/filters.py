from django import forms
import django_filters
from .models import *


class OccupationFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Occupation
        fields = ['name']


class ClientFilter(django_filters.FilterSet):
    """
    Client filter with custom fields, basically all fields from Client will appear on filter.

    The fields phone, birthday, address has some custom inputs.
    phone and birthday has masks (unfortunally you have to make some 'clean up' on these fields, because if empty they will send the masks into value)
    address is a TextField and has an autosize field with overflow as break-word. 
    """

    name = django_filters.CharFilter(lookup_expr='icontains')
    email = django_filters.CharFilter(lookup_expr='icontains')
    # If you wanna use the phone or birthday as filter, uncoment this lines,
    # but be sure to change the get_GET_data method, because for some reason if
    # leave empty the mask will be sent.
    # phone = django_filters.CharFilter(lookup_expr='icontains',
    #                                   widget=forms.TextInput(
    #                                       attrs={"data-mask": "(00) 0 0000-0000", "data-mask-visible": True, "placeholder": "(00) 0 0000-0000", "autocomplete": "off"}))
    # birthday = django_filters.DateFilter(widget=forms.TextInput(
    #     attrs={"data-mask": "00/00/0000", "data-mask-visible": True, "placeholder": "00/00/0000", "autocomplete": "off"}))
    address = django_filters.CharFilter(lookup_expr='icontains',
                                        widget=forms.Textarea(
                                            attrs={"rows": 1, "data-bs-toggle": "autosize", "style": "overflow: hidden; overflow-wrap: break-word; resize: none;"}))

    class Meta:
        model = Client
        fields = ['name', 'email', 'address', 'occupation']
