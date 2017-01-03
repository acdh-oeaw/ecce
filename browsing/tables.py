import django_tables2 as tables
from django_tables2.utils import A
from tokens.models import Token


class TokenTable(tables.Table):
    id = tables.Column(verbose_name='ID')
    legacy_id = tables.LinkColumn(
        'tokens:token_detail',
        args=[A('pk')], verbose_name='Token'
    )
    cluster = tables.LinkColumn(
        'tokens:cluster_detail',
        args=[A('cluster.id')]
    )

    class Meta:
        model = Token
        fields = ['legacy_id']
        attrs = {"class": "table table-hover table-striped table-condensed"}
