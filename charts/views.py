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
from .chart_config import TOKEN_CHART_CONF


class ChartSelector(TemplateView):

    template_name = 'charts/select_chart.html'

    def get_context_data(self, **kwargs):
        context = super(ChartSelector, self).get_context_data()
        context['links'] = TOKEN_CHART_CONF
        return context


class DynChartView(GenericListView):

    model = Token
    table_class = TokenTable
    filter_class = TokenListFilter
    formhelper_class = TokenFilterFormHelper
    template_name = 'charts/dynchart.html'

    def get_context_data(self, **kwargs):
        context = super(DynChartView, self).get_context_data()
        context[self.context_filter_name] = self.filter
        context['charttype'] = self.kwargs['charttype']
        property_name = self.kwargs['property']
        plotted_item = TOKEN_CHART_CONF[property_name]
        payload = {}
        objects = self.get_queryset()
        for x in objects.values(property_name).annotate(
                amount=Count(property_name)).order_by('amount'):
            payload[x[property_name]] = x['amount']
        context['all'] = Token.objects.count()
        data = {
            "items": "{} out of {}".format(objects.count(), context['all']),
            "title": "Tokens per {}".format(plotted_item['label']),
            "subtitle": "Tokens per {}".format(plotted_item['help_text']),
            "legendx": property_name.title(),
            "legendy": "# of Tokens",
            "categories": "sorted(dates)",
            "measuredObject": "Tokens",
            "ymin": 0,
            "payload": payload
        }
        context['data'] = data

        return context
