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
        widgets = {
            'genre': autocomplete.ModelSelect2(
                url='../../../vocabs/skos-ac-filtered/?scheme=ecce-genre'),
            'dialect': autocomplete.ModelSelect2(
                url='../../../vocabs/skos-ac-filtered/?scheme=ecce-dialect'),
        }

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
        widgets = {
            'art_manner': autocomplete.ModelSelect2(
                url='../../../vocabs/skos-ac-filtered/?scheme=ecce-artManner'),
            'art_place': autocomplete.ModelSelect2(
                url='../../../vocabs/skos-ac-filtered/?scheme=ecce-artPlace'),
            'voice': autocomplete.ModelSelect2(
                url='../../../vocabs/skos-ac-filtered/?scheme=ecce-voice'),
            'airflow': autocomplete.ModelSelect2(
                url='../../../vocabs/skos-ac-filtered/?scheme=ecce-airflow'),
        }

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
        widgets = {
            'morphonotacticity': autocomplete.ModelSelect2(
                url='../../../vocabs/skos-ac-filtered/?scheme=ecce-morphonotacticity'),
        }

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
        widgets = {
            'schwaprese': autocomplete.ModelSelect2(
                url='../../../vocabs/skos-ac-filtered/?scheme=ecce-schwapresent'),
        }

    def __init__(self, *args, **kwargs):
        super(SchwaPresentForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-3'
        self.helper.field_class = 'col-md-9'
        self.helper.add_input(Submit('submit', 'save'),)


class OnSetForm(forms.ModelForm):
    class Meta:
        model = OnSet
        fields = "__all__"
        widgets = {
            'variable': autocomplete.ModelSelect2(
                url='../../../vocabs/skos-ac-filtered/?scheme=ecce-variable'),
        }

    def __init__(self, *args, **kwargs):
        super(OnSetForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-3'
        self.helper.field_class = 'col-md-9'
        self.helper.add_input(Submit('submit', 'save'),)


class TokenForm(forms.ModelForm):
    class Meta:
        model = Token
        fields = "__all__"
        widgets = {
            'pos': autocomplete.ModelSelect2(
                url='../../../vocabs/skos-ac-filtered/?scheme=ecce-pos'),
        }

    def __init__(self, *args, **kwargs):
        super(TokenForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-3'
        self.helper.field_class = 'col-md-9'
        self.helper.add_input(Submit('submit', 'save'),)
