import django_filters
from django_filters import DateRangeFilter, DateFilter, DateFromToRangeFilter
from django_filters.widgets import RangeWidget
from dal import autocomplete
from tokens.models import *
from vocabs.models import SkosConcept
import re


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


def build_consonant_choices():
    cons = Consonant.objects.all()
    cons_dict = [('NULL', 'NO VALUE')]
    try:
        for x in cons:
            new = (x.id, x.consonant)
            cons_dict.append(new)
    except:
        pass
    return cons_dict


CONS_CHOICES = build_consonant_choices()


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
    lemma__name = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=Lemma._meta.get_field('name').help_text,
        label=Lemma._meta.get_field('name').verbose_name
        )
    lemma__pos = django_filters.ModelMultipleChoiceFilter(
        queryset = SkosConcept.objects.filter(scheme__dc_title__iexact='ecce-pos'),
        help_text=Lemma._meta.get_field('pos').help_text,
        label=Lemma._meta.get_field('pos').verbose_name
        )
    pos = django_filters.ModelMultipleChoiceFilter(
        queryset=SkosConcept.objects.filter(scheme__dc_title__iexact='ecce-pos'),
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
    # label__label = django_filters.ModelMultipleChoiceFilter(
    #     queryset=TokenLabel.objects.all(),
    #     help_text=TokenLabel._meta.get_field('label').help_text,
    #     label=TokenLabel._meta.get_field('label').verbose_name
    #     )
    label__description = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=TokenLabel._meta.get_field('description').help_text,
        label=TokenLabel._meta.get_field('description').verbose_name
        )
    label__morphonotacticity = django_filters.ModelMultipleChoiceFilter(
        queryset=SkosConcept.objects.filter(scheme__dc_title__iexact='morphonotacticity'),
        help_text=TokenLabel._meta.get_field('morphonotacticity').help_text,
        label=TokenLabel._meta.get_field('morphonotacticity').verbose_name
        )
    rightonset = django_filters.ModelMultipleChoiceFilter(
        queryset=OnSet.objects.all(),
        help_text=Token._meta.get_field('rightonset').help_text,
        label=Token._meta.get_field('rightonset').verbose_name
        )
    rightonset__variable = django_filters.ModelMultipleChoiceFilter(
        queryset=SkosConcept.objects.filter(scheme__dc_title__iexact='ecce-variable'),
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
    weight_norm = django_filters.NumberFilter(
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
    text_source__genre = django_filters.ModelMultipleChoiceFilter(
        queryset=SkosConcept.objects.filter(scheme__dc_title__iexact='ecce-genre'),
        help_text=Text._meta.get_field('genre').help_text,
        label=Text._meta.get_field('genre').verbose_name
        )
    text_source__corpus = django_filters.ModelMultipleChoiceFilter(
        queryset=Corpus.objects.all(),
        help_text=Text._meta.get_field('corpus').help_text,
        label=Text._meta.get_field('corpus').verbose_name
        )
    text_source__mean_date = django_filters.ModelMultipleChoiceFilter(
        queryset=Date.objects.all(),
        help_text=Text._meta.get_field('mean_date').help_text,
        label=Text._meta.get_field('mean_date').verbose_name
        )
    text_source__size = django_filters.NumberFilter(
        lookup_expr='exact',
        help_text=Text._meta.get_field('size').help_text,
        label=Text._meta.get_field('size').verbose_name
        )
    text_source__dialect = django_filters.ModelMultipleChoiceFilter(
        queryset=SkosConcept.objects.filter(scheme__dc_title__iexact='ecce-dialect'),
        help_text=Text._meta.get_field('dialect').help_text,
        label=Text._meta.get_field('dialect').verbose_name
        )
    text_source = django_filters.ModelMultipleChoiceFilter(
        queryset=Text.objects.all(),
        help_text=Token._meta.get_field('text_source').help_text,
        label=Token._meta.get_field('text_source').verbose_name
        )
    text_source__mean_date__decade = django_filters.NumberFilter(
        lookup_expr='exact',
        help_text=Date._meta.get_field('decade').help_text,
        label=Date._meta.get_field('decade').verbose_name
        )
    text_source__mean_date__semicentury = django_filters.NumberFilter(
        lookup_expr='exact',
        help_text=Date._meta.get_field('semicentury').help_text,
        label=Date._meta.get_field('semicentury').verbose_name
        )
    text_source__mean_date__century = django_filters.NumberFilter(
        lookup_expr='exact',
        help_text=Date._meta.get_field('century').help_text,
        label=Date._meta.get_field('century').verbose_name
        )

    class Meta:
        model = Token
        fields = [
            'legacy_id'
        ]


class LemmaListFilter(django_filters.FilterSet):

    class Meta:
        model = Lemma
        fields = "__all__"


class DateListFilter(django_filters.FilterSet):

    class Meta:
        model = Date
        fields = "__all__"


class CorpusListFilter(django_filters.FilterSet):

    class Meta:
        model = Corpus
        fields = "__all__"


class TextListFilter(django_filters.FilterSet):
    genre = django_filters.ModelMultipleChoiceFilter(
        queryset=SkosConcept.objects.filter(scheme__dc_title__iexact='ecce-genre'),
        help_text=Text._meta.get_field('genre').help_text,
        label=Text._meta.get_field('genre').verbose_name
        )
    dialect = django_filters.ModelMultipleChoiceFilter(
        queryset=SkosConcept.objects.filter(scheme__dc_title__iexact='ecce-dialect'),
        help_text=Text._meta.get_field('dialect').help_text,
        label=Text._meta.get_field('dialect').verbose_name
        )

    class Meta:
        model = Text
        fields = "__all__"


class ConsonantListFilter(django_filters.FilterSet):
    art_manner = django_filters.ModelMultipleChoiceFilter(
        queryset=SkosConcept.objects.filter(scheme__dc_title__iexact='ecce-artManner'),
        help_text=Consonant._meta.get_field('art_manner').help_text,
        label=Consonant._meta.get_field('art_manner').verbose_name
        )

    art_place = django_filters.ModelMultipleChoiceFilter(
        queryset=SkosConcept.objects.filter(scheme__dc_title__iexact='ecce-artPlace'),
        help_text=Consonant._meta.get_field('art_place').help_text,
        label=Consonant._meta.get_field('art_place').verbose_name
        )

    voice = django_filters.ModelMultipleChoiceFilter(
        queryset=SkosConcept.objects.filter(scheme__dc_title__iexact='ecce-voice'),
        help_text=Consonant._meta.get_field('voice').help_text,
        label=Consonant._meta.get_field('voice').verbose_name
        )

    airflow = django_filters.ModelMultipleChoiceFilter(
        queryset=SkosConcept.objects.filter(scheme__dc_title__iexact='ecce-airflow'),
        help_text=Consonant._meta.get_field('airflow').help_text,
        label=Consonant._meta.get_field('airflow').verbose_name
        )

    class Meta:
        model = Consonant
        fields = "__all__"


class ClusterListFilter(django_filters.FilterSet):

    class Meta:
        model = Cluster
        fields = "__all__"


class TokenLabelListFilter(django_filters.FilterSet):
    morphonotacticity = django_filters.ModelMultipleChoiceFilter(
        queryset=SkosConcept.objects.filter(scheme__dc_title__iexact='morphonotacticity'),
        help_text=TokenLabel._meta.get_field('morphonotacticity').help_text,
        label=TokenLabel._meta.get_field('morphonotacticity').verbose_name
        )

    class Meta:
        model = TokenLabel
        fields = "__all__"


class SchwaPresentListFilter(django_filters.FilterSet):
    schwaprese = django_filters.ModelMultipleChoiceFilter(
        queryset=SkosConcept.objects.filter(scheme__dc_title__iexact='schwapresent'),
        help_text=SchwaPresent._meta.get_field('schwaprese').help_text,
        label=SchwaPresent._meta.get_field('schwaprese').verbose_name
        )

    class Meta:
        model = SchwaPresent
        fields = "__all__"


class OnSetListFilter(django_filters.FilterSet):
    variable = django_filters.ModelMultipleChoiceFilter(
        queryset=SkosConcept.objects.filter(scheme__dc_title__iexact='ecce-variable'),
        help_text=OnSet._meta.get_field('variable').help_text,
        label=OnSet._meta.get_field('variable').verbose_name
        )

    class Meta:
        model = OnSet
        fields = "__all__"


class TokenCustomFilter(django_filters.FilterSet):
    #Consonants
    cluster__first_consonant__consonant = django_filters.ChoiceFilter(
        choices=CONS_CHOICES,
        label="C1",
        method='filter_by_null',
        empty_label="ANY PHONEME"
        )
    cluster__second_consonant__consonant = django_filters.ChoiceFilter(
        choices=CONS_CHOICES,
        label="C2",
        method='filter_by_null',
        empty_label="ANY PHONEME"
        )
    cluster__third_consonant__consonant = django_filters.ChoiceFilter(
        choices=CONS_CHOICES,
        label="C3",
        method='filter_by_null',
        empty_label="ANY PHONEME"
        )
    cluster__fourth_consonant__consonant = django_filters.ChoiceFilter(
        choices=CONS_CHOICES,
        label="C4",
        method='filter_by_null',
        empty_label="ANY PHONEME"
        )
    #Art manner
    cluster__first_consonant__art_manner = django_filters.ModelChoiceFilter(
        queryset=SkosConcept.objects.filter(scheme__dc_title__iexact='ecce-artManner'),
        label=""
        )
    cluster__second_consonant__art_manner = django_filters.ModelChoiceFilter(
        queryset=SkosConcept.objects.filter(scheme__dc_title__iexact='ecce-artManner'),
        label=""
        )
    cluster__third_consonant__art_manner = django_filters.ModelChoiceFilter(
        queryset=SkosConcept.objects.filter(scheme__dc_title__iexact='ecce-artManner'),
        label=""
        )
    cluster__fourth_consonant__art_manner = django_filters.ModelChoiceFilter(
        queryset=SkosConcept.objects.filter(scheme__dc_title__iexact='ecce-artManner'),
        label=""
        )
    #Art place
    cluster__first_consonant__art_place = django_filters.ModelChoiceFilter(
        queryset=SkosConcept.objects.filter(scheme__dc_title__iexact='ecce-artPlace'),
        label=""
        )
    cluster__second_consonant__art_place = django_filters.ModelChoiceFilter(
        queryset=SkosConcept.objects.filter(scheme__dc_title__iexact='ecce-artPlace'),
        label=""
        )
    cluster__third_consonant__art_place = django_filters.ModelChoiceFilter(
        queryset=SkosConcept.objects.filter(scheme__dc_title__iexact='ecce-artPlace'),
        label=""
        )
    cluster__fourth_consonant__art_place = django_filters.ModelChoiceFilter(
        queryset=SkosConcept.objects.filter(scheme__dc_title__iexact='ecce-artPlace'),
        label=""
        )
    #Voice
    cluster__first_consonant__voice = django_filters.ModelChoiceFilter(
        queryset=SkosConcept.objects.filter(scheme__dc_title__iexact='ecce-voice'),
        label=""
        )
    cluster__second_consonant__voice = django_filters.ModelChoiceFilter(
        queryset=SkosConcept.objects.filter(scheme__dc_title__iexact='ecce-voice'),
        label=""
        )
    cluster__third_consonant__voice = django_filters.ModelChoiceFilter(
        queryset=SkosConcept.objects.filter(scheme__dc_title__iexact='ecce-voice'),
        label=""
        )
    cluster__fourth_consonant__voice = django_filters.ModelChoiceFilter(
        queryset=SkosConcept.objects.filter(scheme__dc_title__iexact='ecce-voice'),
        label=""
        )
    #Period
    text_source__mean_date__dates = django_filters.NumericRangeFilter(
        lookup_expr='range',
        label="",
        widget=RangeWidget(attrs={'placeholder': 'YYYY'})
        )
    #Search spelling string
    plain_word = django_filters.CharFilter(
        method='filter_wildcard',
        label="",
        help_text='use + as a wildcard when needed'
        )
    #MPT Status
    label = django_filters.ModelChoiceFilter(
        queryset=TokenLabel.objects.all(),
        label=""
        )
    #POS
    pos = django_filters.ModelMultipleChoiceFilter(
        queryset=SkosConcept.objects.filter(scheme__dc_title__iexact='ecce-pos'),
        label=""
        )
    #All filters from the ToeknListFilter
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
    lemma__name = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=Lemma._meta.get_field('name').help_text,
        label=Lemma._meta.get_field('name').verbose_name
        )
    lemma__pos = django_filters.ModelMultipleChoiceFilter(
        queryset = SkosConcept.objects.filter(scheme__dc_title__iexact='ecce-pos'),
        help_text=Lemma._meta.get_field('pos').help_text,
        label=Lemma._meta.get_field('pos').verbose_name
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
    label__description = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=TokenLabel._meta.get_field('description').help_text,
        label=TokenLabel._meta.get_field('description').verbose_name
        )
    label__morphonotacticity = django_filters.ModelMultipleChoiceFilter(
        queryset=SkosConcept.objects.filter(scheme__dc_title__iexact='morphonotacticity'),
        help_text=TokenLabel._meta.get_field('morphonotacticity').help_text,
        label=TokenLabel._meta.get_field('morphonotacticity').verbose_name
        )
    rightonset = django_filters.ModelMultipleChoiceFilter(
        queryset=OnSet.objects.all(),
        help_text=Token._meta.get_field('rightonset').help_text,
        label=Token._meta.get_field('rightonset').verbose_name
        )
    rightonset__variable = django_filters.ModelMultipleChoiceFilter(
        queryset=SkosConcept.objects.filter(scheme__dc_title__iexact='ecce-variable'),
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
    weight_norm = django_filters.NumberFilter(
        lookup_expr='exact',
        help_text=Token._meta.get_field('weight_norm').help_text,
        label=Token._meta.get_field('weight_norm').verbose_name
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
    text_source__genre = django_filters.ModelMultipleChoiceFilter(
        queryset=SkosConcept.objects.filter(scheme__dc_title__iexact='ecce-genre'),
        help_text=Text._meta.get_field('genre').help_text,
        label=Text._meta.get_field('genre').verbose_name
        )
    text_source__corpus = django_filters.ModelMultipleChoiceFilter(
        queryset=Corpus.objects.all(),
        help_text=Text._meta.get_field('corpus').help_text,
        label=Text._meta.get_field('corpus').verbose_name
        )
    text_source__size = django_filters.NumberFilter(
        lookup_expr='exact',
        help_text=Text._meta.get_field('size').help_text,
        label=Text._meta.get_field('size').verbose_name
        )
    text_source__dialect = django_filters.ModelMultipleChoiceFilter(
        queryset=SkosConcept.objects.filter(scheme__dc_title__iexact='ecce-dialect'),
        help_text=Text._meta.get_field('dialect').help_text,
        label=Text._meta.get_field('dialect').verbose_name
        )
    text_source = django_filters.ModelMultipleChoiceFilter(
        queryset=Text.objects.all(),
        help_text=Token._meta.get_field('text_source').help_text,
        label=Token._meta.get_field('text_source').verbose_name
        )
    text_source__mean_date__decade = django_filters.NumberFilter(
        lookup_expr='exact',
        help_text=Date._meta.get_field('decade').help_text,
        label=Date._meta.get_field('decade').verbose_name
        )
    text_source__mean_date__semicentury = django_filters.NumberFilter(
        lookup_expr='exact',
        help_text=Date._meta.get_field('semicentury').help_text,
        label=Date._meta.get_field('semicentury').verbose_name
        )
    text_source__mean_date__century = django_filters.NumberFilter(
        lookup_expr='exact',
        help_text=Date._meta.get_field('century').help_text,
        label=Date._meta.get_field('century').verbose_name
        )


    def filter_by_null(self, qs, name, value):
        if value == 'NULL':
            lookup = '__'.join([name, 'isnull'])
            qs = qs.filter(**{lookup: True})
        else:
            print("NO EMTPY LABEL")
            lookup = name.replace('__consonant', '__id')
            qs = qs.filter(**{lookup: value})
        return qs


    def filter_wildcard(self, qs, name, value):
        #for cases like '+c+' - query all words with 'c' inside the word
        if value.startswith('+') and value.endswith('+'):
            newvalue = value[1:-1]
            qs = qs.filter(plain_word__icontains=newvalue)\
            .exclude(plain_word__istartswith=newvalue)\
            .exclude(plain_word__iendswith=newvalue)
        #for cases like '+nd' - query all words which end with 'nd'
        elif value.startswith('+'):
            newvalue = value.split('+')[1]
            qs = qs.filter(plain_word__iendswith=newvalue)
        #for cases like 'a+' - query all words which start with 'a'
        elif value.endswith('+'):
            newvalue = value.split('+')[0]
            qs = qs.filter(plain_word__istartswith=newvalue)
        else:
            #for cases like 's+e' - query all words which start with 's' and end with 'e'
            if '+' in value:
                newvalue = value.split('+')
                startvalue = newvalue[0]
                endvalue = newvalue[-1]
                qs = qs.filter(plain_word__istartswith=startvalue)\
                .filter(plain_word__iendswith=endvalue)
            else:
                #for all rest cases including whole word search
                qs = qs.filter(plain_word__icontains=value)
        return qs


    class Meta:
        model = Token
        fields = [
            'legacy_id'
        ]
