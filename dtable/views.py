from browsing.views import GenericListView
from .models import NormToken
from browsing.tables import NormTokenTable
from browsing.filters import NormTokenListFilter
from browsing.forms import GenericFilterFormHelper


class DynChartView(GenericListView):
    model = NormToken
    table_class = NormTokenTable
    template_name = 'dtable/dynchart.html'
    filter_class = NormTokenListFilter
    formhelper_class = GenericFilterFormHelper

    def get_context_data(self, **kwargs):
        context = super(GenericListView, self).get_context_data()
        context[self.context_filter_name] = self.filter
        data = {
            "items": len(self.filter),
            "title": "Tokens per semicentury",
            "subtitle": "Tokens per semicentury",
            "legendx": "Semicentury",
            "legendy": "# of Tokens",
            "categories": "sorted(dates)",
            "measuredObject": "Tokens",
            "ymin": 0,
        }
        context['amount'] = data
        return context
