from django import forms
from django.conf import settings
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Div, Layout, Row, Field
from crispy_forms.bootstrap import PrependedText, AppendedText
from django.utils.translation import gettext as _

from .models import *


class TypeOfServiceForm(forms.ModelForm):

    id = forms.IntegerField(initial=0)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.form_class = 'form-control'
        self.fields['id'].widget = forms.HiddenInput()

    class Meta:
        model = TypeOfService
        fields = '__all__'


class DomainForm(forms.ModelForm):

    id = forms.IntegerField(initial=0)
    acquisition_date = forms.DateField(localize=True, required=False,
                                       widget=forms.TextInput(
                                           attrs={"data-mask": "00/00/0000", "data-mask-visible": True, "placeholder": "00/00/0000", "autocomplete": "off"}))

    layout = Layout(
        Div(
            Field('id', type='hidden'),
            Row(
                Field('name', wrapper_class="col-lg-6 col-sm-12"),
                Field('link', wrapper_class="col-lg-6 col-sm-12"),
            ),
            Row(
                Field('acquisition_date', wrapper_class="col-md-4 col-sm-12"),
                Field('contract', wrapper_class="col-md-8 col-sm-12"),
            ),
        ),
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = self.layout
        self.helper.form_class = 'form-control'

    class Meta:
        model = Domain
        widgets = {
            'link': forms.Textarea(attrs={"rows": 1, "data-bs-toggle": "autosize", "style": "overflow: hidden; overflow-wrap: break-word; resize: none;"}),
        }
        fields = '__all__'


class ContractForm(forms.ModelForm):

    id = forms.IntegerField(initial=0)
    start_date = forms.DateField(localize=True, required=False,
                                 widget=forms.TextInput(
                                     attrs={"data-mask": "00/00/0000", "data-mask-visible": True, "placeholder": "00/00/0000", "autocomplete": "off"}))

    layout = Layout(
        Div(
            Field('id', type='hidden'),
            Row(
                PrependedText(
                    'value', settings.MONEY_SYMBOL, wrapper_class="col-lg-6 col-sm-12"
                ),
                Field('start_date', wrapper_class="col-lg-6 col-sm-12"),
            ),
            Row(
                AppendedText(
                    'expiration', _("Month"),
                    wrapper_class="col-md-4 col-sm-12"
                ),
                Field('attachment', wrapper_class="col-md-8 col-sm-12"),
            ),
            Field('description'),
        ),
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = self.layout
        self.helper.form_class = 'form-control'

    class Meta:
        model = Contract
        widgets = {
            'description': forms.Textarea(attrs={"rows": 1, "data-bs-toggle": "autosize", "style": "overflow: hidden; overflow-wrap: break-word; resize: none;"}),
        }
        fields = '__all__'


class WebServiceForm(forms.ModelForm):

    id = forms.IntegerField(initial=0)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.form_class = 'form-control'
        self.fields['id'].widget = forms.HiddenInput()

    class Meta:
        model = WebService
        fields = '__all__'
