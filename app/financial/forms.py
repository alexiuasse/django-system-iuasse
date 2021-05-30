from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Div, Layout, Row, Field
from crispy_forms.bootstrap import PrependedText

from .models import *


class PaymentStatusForm(forms.ModelForm):

    id = forms.IntegerField(initial=0)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.form_class = 'form-control'
        self.fields['id'].widget = forms.HiddenInput()

    class Meta:
        model = PaymentStatus
        fields = '__all__'


class TypeOfPaymentForm(forms.ModelForm):

    id = forms.IntegerField(initial=0)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.form_class = 'form-control'
        self.fields['id'].widget = forms.HiddenInput()

    class Meta:
        model = TypeOfPayment
        fields = '__all__'


class CostCenterForm(forms.ModelForm):

    id = forms.IntegerField(initial=0)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.form_class = 'form-control'
        self.fields['id'].widget = forms.HiddenInput()

    class Meta:
        model = CostCenter
        fields = '__all__'


class FinancialReleaseForm(forms.ModelForm):

    id = forms.IntegerField(initial=0)

    layout = Layout(
        Div(
            Field('id', type='hidden'),
            Row(
                PrependedText('total_value', 'R$',
                              wrapper_class="col-lg-6 col-sm-12"),
                Field('cost_center', wrapper_class="col-md-6 col-sm-12"),
            ),
            Row(
                Field('type_of_payment', wrapper_class="col-lg-6 col-sm-12"),
                Field('total_parcels', wrapper_class="col-md-6 col-sm-12"),
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
        model = FinancialRelease
        widgets = {
            # 'address': forms.Textarea(attrs={"rows": 1, "data-bs-toggle": "autosize", "style": "overflow: hidden; overflow-wrap: break-word; resize: none;"}),
            # 'phone': forms.TextInput(attrs={"data-mask": "(00) 0 0000-0000", "data-mask-visible": True, "placeholder": "(00) 0 0000-0000", "autocomplete": "off"}),
            # 'birthday': forms.TextInput(attrs={"data-mask": "00/00/0000", "data-mask-visible": True, "placeholder": "00/00/0000", "autocomplete": "off"}),
        }
        fields = '__all__'
