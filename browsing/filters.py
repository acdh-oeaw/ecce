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
    legacy_id = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=Token._meta.get_field('legacy_id').help_text,
        label=Token._meta.get_field('legacy_id').verbose_name
        )
    left_context = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=Token._meta.get_field('left_context').help_text,
        label=Token._meta.get_field('left_context').verbose_name
        )
    plain_word = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=Token._meta.get_field('plain_word').help_text,
        label=Token._meta.get_field('plain_word').verbose_name
        )
    right_context = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=Token._meta.get_field('right_context').help_text,
        label=Token._meta.get_field('right_context').verbose_name
        )
    spelling2 = django_filters.ModelMultipleChoiceFilter(
        queryset=SchwaPresent.objects.all(),
        help_text=Token._meta.get_field('spelling2').help_text,
        label=Token._meta.get_field('spelling2').verbose_name
        )
    lemma = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=Token._meta.get_field('lemma').help_text,
        label=Token._meta.get_field('lemma').verbose_name
        )
    lemma__name = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=Lemma._meta.get_field('name').help_text,
        label=Lemma._meta.get_field('name').verbose_name
        )
    lemma__pos = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=Lemma._meta.get_field('pos').help_text,
        label=Lemma._meta.get_field('pos').verbose_name
        )
    pos = django_filters.ModelMultipleChoiceFilter(
        queryset=SkosConcept.objects.all(),
        help_text=Token._meta.get_field('pos').help_text,
        label=Token._meta.get_field('pos').verbose_name
        )
    label = django_filters.ModelMultipleChoiceFilter(
        queryset=TokenLabel.objects.all(),
        help_text=Token._meta.get_field('label').help_text,
        label=Token._meta.get_field('label').verbose_name
        )
    medial_suffix = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=Token._meta.get_field('medial_suffix').help_text,
        label=Token._meta.get_field('medial_suffix').verbose_name
        )
    final_suffix = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=Token._meta.get_field('final_suffix').help_text,
        label=Token._meta.get_field('final_suffix').verbose_name
        )
    label__label = django_filters.ModelMultipleChoiceFilter(
        queryset=TokenLabel.objects.all(),
        help_text=TokenLabel._meta.get_field('label').help_text,
        label=TokenLabel._meta.get_field('label').verbose_name
        )
    label__description = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=TokenLabel._meta.get_field('description').help_text,
        label=TokenLabel._meta.get_field('description').verbose_name
        )
    label__morphonotacticity = django_filters.ModelMultipleChoiceFilter(
        queryset=TokenLabel.objects.all(),
        help_text=TokenLabel._meta.get_field('morphonotacticity').help_text,
        label=TokenLabel._meta.get_field('morphonotacticity').verbose_name
        )
    rightonset = django_filters.ModelMultipleChoiceFilter(
        queryset=OnSet.objects.all(),
        help_text=Token._meta.get_field('rightonset').help_text,
        label=Token._meta.get_field('rightonset').verbose_name
        )
    rightonset__variable = django_filters.ModelMultipleChoiceFilter(
        queryset=OnSet.objects.all(),
        help_text=OnSet._meta.get_field('variable').help_text,
        label=OnSet._meta.get_field('variable').verbose_name
        )
    rightonset__pre_change = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=OnSet._meta.get_field('pre_change').help_text,
        label=OnSet._meta.get_field('pre_change').verbose_name
        )
    rightonset__post_change = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=OnSet._meta.get_field('post_change').help_text,
        label=OnSet._meta.get_field('post_change').verbose_name
        )
    rightonset__onset = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=OnSet._meta.get_field('onset').help_text,
        label=OnSet._meta.get_field('onset').verbose_name
        )
    rightonset__offset = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=OnSet._meta.get_field('offset').help_text,
        label=OnSet._meta.get_field('offset').verbose_name
        )
    weight = django_filters.NumberFilter(
        lookup_expr='exact',
        help_text=Token._meta.get_field('weight').help_text,
        label=Token._meta.get_field('weight').verbose_name
        )
    weight_norm= django_filters.NumberFilter(
        lookup_expr='exact',
        help_text=Token._meta.get_field('weight_norm').help_text,
        label=Token._meta.get_field('weight_norm').verbose_name
        )
    cluster__consonant = django_filters.ModelMultipleChoiceFilter(
        queryset=Cluster.objects.all(),
        help_text=Cluster._meta.get_field('consonant').help_text,
        label=Cluster._meta.get_field('consonant').verbose_name
        )
    cluster__first_consonant__consonant = django_filters.ModelMultipleChoiceFilter(
        queryset=Consonant.objects.all(),
        help_text=Cluster._meta.get_field('first_consonant').help_text,
        label=Cluster._meta.get_field('first_consonant').verbose_name
        )
    cluster__second_consonant__consonant = django_filters.ModelMultipleChoiceFilter(
        queryset=Consonant.objects.all(),
        help_text=Cluster._meta.get_field('second_consonant').help_text,
        label=Cluster._meta.get_field('second_consonant').verbose_name
        )
    cluster__third_consonant__consonant = django_filters.ModelMultipleChoiceFilter(
        queryset=Consonant.objects.all(),
        help_text=Cluster._meta.get_field('third_consonant').help_text,
        label=Cluster._meta.get_field('third_consonant').verbose_name
        )
    cluster__fourth_consonant__consonant = django_filters.ModelMultipleChoiceFilter(
        queryset=Consonant.objects.all(),
        help_text=Cluster._meta.get_field('fourth_consonant').help_text,
        label=Cluster._meta.get_field('fourth_consonant').verbose_name
        )
    cluster__size = django_filters.NumberFilter(
        lookup_expr='exact',
        help_text=Cluster._meta.get_field('size').help_text,
        label=Cluster._meta.get_field('size').verbose_name
        )
    cluster__ssp = django_filters.NumberFilter(
        lookup_expr='exact',
        help_text=Cluster._meta.get_field('ssp').help_text,
        label=Cluster._meta.get_field('ssp').verbose_name
        )
    cluster__nad_vc = django_filters.NumberFilter(
        lookup_expr='exact',
        help_text=Cluster._meta.get_field('nad_vc').help_text,
        label=Cluster._meta.get_field('nad_vc').verbose_name
        )
    cluster__nad_c1c2 = django_filters.NumberFilter(
        lookup_expr='exact',
        help_text=Cluster._meta.get_field('nad_c1c2').help_text,
        label=Cluster._meta.get_field('nad_c1c2').verbose_name
        )
    cluster__nad_c2c3 = django_filters.NumberFilter(
        lookup_expr='exact',
        help_text=Cluster._meta.get_field('nad_c2c3').help_text,
        label=Cluster._meta.get_field('nad_c2c3').verbose_name
        )
    cluster__preferred_cluster = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=Cluster._meta.get_field('preferred_cluster').help_text,
        label=Cluster._meta.get_field('preferred_cluster').verbose_name
        )


    


    class Meta:
        model = Token
        fields = [
            'legacy_id'
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
