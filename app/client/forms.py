from django import forms
from django.utils import timezone
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Div, Layout, Row, Field

from .models import Client, Occupation


class OccupationForm(forms.ModelForm):

    id = forms.IntegerField(initial=0)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.form_class = 'form-control'
        self.fields['id'].widget = forms.HiddenInput()

    class Meta:
        model = Occupation
        fields = '__all__'


class ClientForm(forms.ModelForm):

    id = forms.IntegerField(initial=0)

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
            Row(
                Field('occupation', wrapper_class="col-md-8 col-sm-12"),
                Field('date', wrapper_class="col-md-4 col-sm-12"),
            ),
        ),
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = self.layout
        self.helper.form_class = 'form-control'
        self.fields['date'].initial = timezone.now()

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
            'date': forms.DateInput(attrs={"data-mask": "00/00/0000", "data-mask-visible": True, "placeholder": "00/00/0000", "autocomplete": "off"}),
            'birthday': forms.DateInput(attrs={"data-mask": "00/00/0000", "data-mask-visible": True, "placeholder": "00/00/0000", "autocomplete": "off"})
        }
        fields = '__all__'
