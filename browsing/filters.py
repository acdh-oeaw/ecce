import django_filters
from dal import autocomplete
from tokens.models import *
from dtable.models import NormToken
from vocabs.models import SkosConcept

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


class NormTokenListFilter(django_filters.FilterSet):

    class Meta:
        model = NormToken


class TokenListFilter(django_filters.FilterSet):
    # plain_word = django_filters.ModelMultipleChoiceFilter(
    #     widget=autocomplete.Select2Multiple(url='dal_ac:tokenM-ac'),
    #     queryset=Token.objects.all(),
    #     lookup_expr='icontains',
    #     label='Token',
    #     help_text=False,
    # )
    cluster = django_filters.ModelMultipleChoiceFilter(
        queryset=Cluster.objects.all(),
        lookup_expr='icontains',
        label='Cluster',
        help_text=False,
        widget=autocomplete.ModelSelect2Multiple(url='dal_ac:cluster-ac')
    )
    text_source__genre = django_filters.ModelMultipleChoiceFilter(
        queryset=SkosConcept.objects.filter(scheme__dc_title='ecce-genre'),
        lookup_expr='icontains',
        label='Genre',
        help_text=False,
    )
    text_source__mean_date = django_filters.ModelMultipleChoiceFilter(
        queryset=Date.objects.all(),
        lookup_expr='icontains',
        label='Mean Date',
        help_text=False
    )
    text_source = django_filters.ModelMultipleChoiceFilter(
        queryset=Text.objects.all(),
        lookup_expr='icontains',
        label='Text',
        help_text=False
    )
    label = django_filters.ModelMultipleChoiceFilter(
        queryset=TokenLabel.objects.all(),
        lookup_expr='icontains',
        label='Label',
        help_text=False,
    )
    rightonset = django_filters.ModelMultipleChoiceFilter(
        queryset=OnSet.objects.all(),
        lookup_expr='icontains',
        label='OnSet',
        help_text=False,
    )

    class Meta:
        model = Token
        fields = [
            'text_source__mean_date', 'text_source__mean_date__century', 'text_source',
            'text_source__genre', 'label', 'rightonset', 'plain_word', 'cluster', 'cluster__size'
        ]


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
