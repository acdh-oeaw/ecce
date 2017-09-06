import json
from django.db.models import Count
from django.views.generic.list import ListView
from .models import ChartConfig
from .chart_config import TOKEN_CHART_CONF
from browsing.views import GenericListView
from tokens.models import Token
from browsing.tables import TokenTable
from browsing.filters import TokenListFilter
from browsing.forms import TokenFilterFormHelper
from vocabs.models import *


class ChartSelector(ListView):
    model = ChartConfig
    template_name = 'charts/select_chart.html'


class DynChartView(GenericListView):

    model = Token
    table_class = TokenTable
    filter_class = TokenListFilter
    formhelper_class = TokenFilterFormHelper
    template_name = 'charts/dynchart.html'

    def get_context_data(self, **kwargs):
        context = super(DynChartView, self).get_context_data()
        property_name = self.kwargs['property']
        context['property_name'] = property_name
        try:
            chart = ChartConfig.objects.get(
                field_path=self.kwargs['property']
            )
        except:
            context['error'] = True
            return context

        context[self.context_filter_name] = self.filter
        context['charttype'] = self.kwargs['charttype']
        modelname = self.model.__name__
        payload = []
        objects = self.get_queryset()
        for x in objects.values(property_name).annotate(
                amount=Count(property_name)).order_by(property_name):
            if x[property_name]:
                payload.append([x[property_name], x['amount']])
            else:
                payload.append(['None', x['amount']])
        context['all'] = self.model.objects.count()
        if chart.legend_x:
            legendx = chart.legend_x
        else:
            legendx = "# of {}s".format(modelname)
        data = {
            "items": "{} out of {}".format(objects.count(), context['all']),
            "title": "{}".format(chart.label),
            "subtitle": "{}".format(chart.help_text),
            "legendy": chart.legend_y,
            "legendx": legendx,
            "categories": "sorted(dates)",
            "measuredObject": "{}s".format(modelname),
            "ymin": 0,
            "payload": payload
        }
        context['data'] = data

        return context
