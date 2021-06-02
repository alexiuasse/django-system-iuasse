from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Div, Layout, Row, Field
from django.utils.translation import gettext as _
from crispy_forms.bootstrap import PrependedText, AppendedText

from .models import *


class DashboardSettingsForm(forms.ModelForm):

    id = forms.IntegerField(initial=0)

    layout = Layout(
        Div(
            Field('id'),
            AppendedText(
                'contract_warning_days', _("Days"),
                wrapper_class="col-lg-6 col-sm-12"
            ),
            Row(
                PrependedText(
                    'month_earn_goal', settings.MONEY_SYMBOL, wrapper_class="col-lg-6 col-sm-12"
                ),
                PrependedText(
                    'year_earn_goal', settings.MONEY_SYMBOL, wrapper_class="col-lg-6 col-sm-12"
                ),
            ),
        ),
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = self.layout
        self.helper.form_class = 'form-control'
        self.fields['id'].widget = forms.HiddenInput()

    class Meta:
        model = DashboardSettings
        fields = '__all__'
