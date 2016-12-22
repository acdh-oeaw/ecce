from dal import autocomplete
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import *


class DateForm(forms.ModelForm):
    class Meta:
        model = Date
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(DateForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-3'
        self.helper.field_class = 'col-md-9'
        self.helper.add_input(Submit('submit', 'save'),)


class CorpusForm(forms.ModelForm):
    class Meta:
        model = Corpus
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(CorpusForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-3'
        self.helper.field_class = 'col-md-9'
        self.helper.add_input(Submit('submit', 'save'),)


class TextForm(forms.ModelForm):
    class Meta:
        model = Text
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(TextForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-3'
        self.helper.field_class = 'col-md-9'
        self.helper.add_input(Submit('submit', 'save'),)


class ConsonantForm(forms.ModelForm):
    class Meta:
        model = Consonant
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(ConsonantForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-3'
        self.helper.field_class = 'col-md-9'
        self.helper.add_input(Submit('submit', 'save'),)


class ClusterForm(forms.ModelForm):
    class Meta:
        model = Cluster
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(ClusterForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-3'
        self.helper.field_class = 'col-md-9'
        self.helper.add_input(Submit('submit', 'save'),)


class TokenLabelForm(forms.ModelForm):
    class Meta:
        model = TokenLabel
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(TokenLabelForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-3'
        self.helper.field_class = 'col-md-9'
        self.helper.add_input(Submit('submit', 'save'),)


class SchwaPresentForm(forms.ModelForm):
    class Meta:
        model = SchwaPresent
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(SchwaPresentForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-3'
        self.helper.field_class = 'col-md-9'
        self.helper.add_input(Submit('submit', 'save'),)
