from django import forms
from django.conf import settings
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Div, Layout, Row, Field, Submit
from .models import Client


class ClientForm(forms.ModelForm):
    prefix = "clientform"

    id = forms.IntegerField(initial=0)
    birthday = forms.DateField(localize=True, required=False,
                               widget=forms.TextInput(
                                   attrs={"data-mask": "00/00/0000", "data-mask-visible": True, "placeholder": "00/00/0000", "autocomplete": "off"}))

    layout = Layout(
        Div(
            Field('id', type='hidden'),
            Row(
                Field('name', wrapper_class="col-lg-6 col-sm-12"),
                Field('email', wrapper_class="col-lg-6 col-sm-12"),
            ),
            Field('address'),
            Row(
                Field('phone', wrapper_class="col-md-6 col-sm-12"),
                Field('birthday', wrapper_class="col-md-6 col-sm-12"),
            ),
            Field('occupation'),
        ),
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = self.layout
        self.helper.form_class = 'form-control'

    def clean_phone(self):
        data = self.cleaned_data['phone']
        if data == "(__) _ ____-____":
            data = ""
        return data

    class Meta:
        model = Client
        widgets = {
            'address': forms.Textarea(attrs={"rows": 1, "data-bs-toggle": "autosize", "style": "overflow: hidden; overflow-wrap: break-word; resize: none;"}),
            'phone': forms.TextInput(attrs={"data-mask": "(00) 0 0000-0000", "data-mask-visible": True, "placeholder": "(00) 0 0000-0000", "autocomplete": "off"}),
            # 'birthday': forms.TextInput(attrs={"data-mask": "00/00/0000", "data-mask-visible": True, "placeholder": "00/00/0000", "autocomplete": "off"}),
        }
        fields = '__all__'
