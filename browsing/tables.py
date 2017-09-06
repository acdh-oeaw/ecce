import django_tables2 as tables
from django_tables2.utils import A
from tokens.models import *


class TokenTable(tables.Table):
    plain_word = tables.LinkColumn(
        'tokens:token_detail',
        args=[A('pk')], verbose_name='Plain Word'
    )
    lemma = tables.RelatedLinkColumn()
    cluster = tables.TemplateColumn(template_name='browsing/tables/cluster.html')
    label = tables.RelatedLinkColumn()
    date = tables.Column(accessor='text_source.date', verbose_name='Date')


    class Meta:
        model = Token
        sequence = ('legacy_id', 'plain_word', 'pos', 'lemma', 'cluster',
                    'label', 'date')
        attrs = {"class": "table table-responsive table-hover"}


class DateTable(tables.Table):
    # id = tables.Column(verbose_name='ID')
    dates = tables.LinkColumn(
        'tokens:date_detail',
        args=[A('pk')], verbose_name='Date'
    )

    class Meta:
        model = Date
        fields = ['dates']
        attrs = {"class": "table table-responsive table-hover"}


class CorpusTable(tables.Table):
    # id = tables.Column(verbose_name='ID')
    name = tables.LinkColumn(
        'tokens:corpus_detail',
        args=[A('pk')], verbose_name='Corpus'
    )

    class Meta:
        model = Corpus
        fields = ['name']
        attrs = {"class": "table table-responsive table-hover"}


class TextTable(tables.Table):
    # id = tables.Column(verbose_name='ID')
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
        attrs = {"class": "table table-responsive table-hover"}


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
        attrs = {"class": "table table-responsive table-hover"}


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
        attrs = {"class": "table table-responsive table-hover"}


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
        attrs = {"class": "table table-responsive table-hover"}


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
        attrs = {"class": "table table-responsive table-hover"}


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
        attrs = {"class": "table table-responsive table-hover"}
