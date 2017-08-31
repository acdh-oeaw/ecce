import json
from django.db.models import Count
from django.views.generic import TemplateView
from collections import Counter
from browsing.views import GenericListView
from tokens.models import Token
from browsing.tables import TokenTable
from browsing.filters import TokenListFilter
from browsing.forms import TokenFilterFormHelper
from vocabs.models import *


class ChartSelector(TemplateView):

    template_name = 'charts/select_chart.html'

    def get_context_data(self, **kwargs):
        context = super(ChartSelector, self).get_context_data()
        values = {}
        for x in TokenListFilter.declared_filters.items():
            values[x[0]] = {'lookup': x[0], 'label': x[1].label}
        context['links'] = values
        return context


class DynChartView(GenericListView):
    model = Token
    table_class = TokenTable
    template_name = 'charts/dynchart.html'
    filter_class = TokenListFilter
    formhelper_class = TokenFilterFormHelper

    def get_lookup_table(self, **kwargs):
        values = {}
        for x in self.filter_class.declared_filters.items():
            values[x[0]] = {'lookup': x[0], 'label': x[1].label}
        return values

    def get_context_data(self, **kwargs):
        context = super(GenericListView, self).get_context_data()
        context[self.context_filter_name] = self.filter
        property_name = (self.kwargs['property'])
        lookup_table = self.get_lookup_table()
        plotted_item = lookup_table[property_name]
        payload = {}
        for x in self.get_queryset().values(property_name).annotate(amount=Count(property_name)):
            payload[x[property_name]] = x['amount']
        context['all'] = Token.objects.count()
        data = {
            "items": "{} out of {}".format(self.filter.count(), context['all']),
            "title": "Tokens per {}".format(plotted_item['label']),
            "subtitle": "Tokens per {}".format(property_name.title()),
            "legendx": property_name.title(),
            "legendy": "# of Tokens",
            "categories": "sorted(dates)",
            "measuredObject": "Tokens",
            "ymin": 0,
            "payload": payload
        }
        context['data'] = data

        return context
