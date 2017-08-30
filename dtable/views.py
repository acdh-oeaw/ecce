import json
from django.db.models import Count
from collections import Counter
from browsing.views import GenericListView
from .models import NormToken
from tokens.models import Token
from browsing.tables import NormTokenTable, TokenTable
from browsing.filters import NormTokenListFilter, TokenListFilter
from browsing.forms import GenericFilterFormHelper, TokenFilterFormHelper
from vocabs.models import *


class DynChartView(GenericListView):
    model = Token
    table_class = TokenTable
    template_name = 'dtable/dynchart.html'
    filter_class = TokenListFilter
    formhelper_class = TokenFilterFormHelper

    def get_context_data(self, **kwargs):
        context = super(GenericListView, self).get_context_data()
        context[self.context_filter_name] = self.filter
        property_name = (self.kwargs['property'])
        payload = {}
        # https://stackoverflow.com/questions/310732/in-django-how-does-one-filter-a-queryset-with-dynamic-field-lookups
        print(kwargs)
        for x in self.get_queryset().values(property_name).annotate(amount=Count(property_name)):
            payload[x[property_name]] = x['amount']

        data = {
            "items": len(self.filter),
            "title": "Tokens per {}".format(property_name.title()),
            "subtitle": "Tokens per {}".format(property_name.title()),
            "legendx": property_name.title(),
            "legendy": "# of Tokens",
            "categories": "sorted(dates)",
            "measuredObject": "Tokens",
            "ymin": 0,
            "payload": payload
        }
        context['data'] = data
        context['all'] = NormToken.objects.count()
        return context
