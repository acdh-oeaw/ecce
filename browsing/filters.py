import django_filters
from dal import autocomplete
from tokens.models import *

django_filters.filters.LOOKUP_TYPES = [
    ('', '---------'),
    ('exact', 'Is equal to'),
    ('iexact', 'Is equal to (case insensitive)'),
    ('not_exact', 'Is not equal to'),
    ('lt', 'Lesser than/before'),
    ('gt', 'Greater than/after'),
    ('gte', 'Greater than or equal to'),
    ('lte', 'Lesser than or equal to'),
    ('startswith', 'Starts with'),
    ('endswith', 'Ends with'),
    ('contains', 'Contains'),
    ('icontains', 'Contains (case insensitive)'),
    ('not_contains', 'Does not contain'),
]


class TokenListFilter(django_filters.FilterSet):
    # cluster = django_filters.CharFilter(
    #     label='Cluster',
    #     help_text=False, widget=autocomplete.ListSelect2(url='dal_ac:cluster-ac')
    # )

    class Meta:
        model = Token
        fields = ['cluster', 'cluster__size', 'text_source', 'text_source__genre', 'text_source__mean_date']


class DateListFilter(django_filters.FilterSet):

    class Meta:
        model = Date


class CorpusListFilter(django_filters.FilterSet):

    class Meta:
        model = Corpus


class TextListFilter(django_filters.FilterSet):

    class Meta:
        model = Text


class ConsonantListFilter(django_filters.FilterSet):

    class Meta:
        model = Consonant


class ClusterListFilter(django_filters.FilterSet):

    class Meta:
        model = Cluster


class TokenLabelListFilter(django_filters.FilterSet):

    class Meta:
        model = TokenLabel


class SchwaPresentListFilter(django_filters.FilterSet):

    class Meta:
        model = SchwaPresent


class OnSetListFilter(django_filters.FilterSet):

    class Meta:
        model = OnSet
