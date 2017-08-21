import django_tables2 as tables
from django_tables2.utils import A
from tokens.models import *
from dtable.models import NormToken


class NormTokenTable(tables.Table):

    class Meta:
        model = NormToken
        fields = [f.name for f in NormToken._meta.get_fields()]
        attrs = {"class": "table table-responsive table-hover table-striped table-condensed"}


class TokenTable(tables.Table):
    cluster = tables.RelatedLinkColumn(verbose_name='Cluster')
    plain_word = tables.LinkColumn(
        'tokens:token_detail',
        args=[A('pk')], verbose_name='Plain Word'
    )

    class Meta:
        model = Token
        fields = [
            'left_context', 'plain_word', 'pos', 'right_context',
            'cluster', 'medial_suffix', 'final_suffix', 'spelling2'
        ]
        attrs = {"class": "table table-responsive table-hover table-striped table-condensed"}


class DateTable(tables.Table):
    # id = tables.Column(verbose_name='ID')
    dates = tables.LinkColumn(
        'tokens:date_detail',
        args=[A('pk')], verbose_name='Date'
    )

    class Meta:
        model = Date
        fields = ['dates']
        attrs = {"class": "table table-responsive table-hover table-striped table-condensed"}


class CorpusTable(tables.Table):
    #id = tables.Column(verbose_name='ID')
    name = tables.LinkColumn(
        'tokens:corpus_detail',
        args=[A('pk')], verbose_name='Corpus'
    )

    class Meta:
        model = Corpus
        fields = ['name']
        attrs = {"class": "table table-responsive table-hover table-striped table-condensed"}


class TextTable(tables.Table):
    #id = tables.Column(verbose_name='ID')
    text = tables.LinkColumn(
        'tokens:text_detail',
        args=[A('pk')], verbose_name='Text'
    )
    date = tables.Column(
        verbose_name="Date"
    )

    class Meta:
        model = Text
        fields = ['text', 'date']
        attrs = {"class": "table table-responsive table-hover table-striped table-condensed"}


class ConsonantTable(tables.Table):
    consonant = tables.LinkColumn(
        'tokens:consonant_detail',
        args=[A('pk')], verbose_name='Consonant'
    )

    class Meta:
        model = Consonant
        fields = [
            'consonant', 'first_consonant', 'second_consonant',
            'third_consonant', 'fourth_consonant'
        ]
        attrs = {"class": "table table-responsive table-hover table-striped table-condensed"}


class ClusterTable(tables.Table):
    id = tables.LinkColumn(
        'tokens:cluster_detail',
        args=[A('pk')], verbose_name='ID'
    )
    consonant = tables.Column(
        verbose_name='Consonant'
    )
    first_consonant = tables.RelatedLinkColumn(verbose_name='1st')
    second_consonant = tables.RelatedLinkColumn(verbose_name='2nd')
    third_consonant = tables.RelatedLinkColumn(verbose_name='3rd')
    fourth_consonant = tables.RelatedLinkColumn(verbose_name='4th')
    related_tokens_amount = tables.Column(verbose_name='#related Tokens', orderable=False)

    class Meta:
        model = Cluster
        fields = ['id', 'consonant']
        attrs = {"class": "table table-responsive table-hover table-striped table-condensed"}


class TokenLabelTable(tables.Table):
    id = tables.LinkColumn(
        'tokens:tokenlabel_detail',
        args=[A('pk')], verbose_name='ID'
    )
    label = tables.LinkColumn(
        'tokens:tokenlabel_detail',
        args=[A('pk')], verbose_name='Label'
        # attrs={'td': {'class': 'tokenlabel'}},
    )

    class Meta:
        model = TokenLabel
        fields = ['id', 'label']
        attrs = {"class": "table table-responsive table-hover table-striped table-condensed"}


class SchwaPresentTable(tables.Table):
    id = tables.LinkColumn(
        'tokens:schwapresent_detail',
        args=[A('pk')], verbose_name='ID'
    )
    spelling = tables.Column(
        verbose_name='Spelling'
    )
    schwaprese = tables.Column(
        verbose_name='Schwaprese'
    )

    class Meta:
        model = SchwaPresent
        fields = ['id', 'spelling', 'schwaprese']
        attrs = {"class": "table table-responsive table-hover table-striped table-condensed"}


class OnSetTable(tables.Table):
    id = tables.LinkColumn(
        'tokens:onset_detail',
        args=[A('pk')], verbose_name='ID'
    )
    rightonset = tables.Column(
        verbose_name='Rightonset'
    )
    variable = tables.Column(
        verbose_name='Variable'
    )

    class Meta:
        model = OnSet
        fields = ['id', 'rightonset', 'variable']
        attrs = {"class": "table table-responsive table-hover table-striped table-condensed"}
