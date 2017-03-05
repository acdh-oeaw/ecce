import json
from collections import Counter
from browsing.views import GenericListView
from .models import NormToken
from browsing.tables import NormTokenTable
from browsing.filters import NormTokenListFilter
from browsing.forms import GenericFilterFormHelper
from vocabs.models import *


class DynChartView(GenericListView):
    model = NormToken
    table_class = NormTokenTable
    template_name = 'dtable/dynchart.html'
    filter_class = NormTokenListFilter
    formhelper_class = GenericFilterFormHelper

    def get_context_data(self, **kwargs):
        context = super(GenericListView, self).get_context_data()
        context[self.context_filter_name] = self.filter
        property_name = (self.kwargs['property'])
        if len(self.request.GET) > 0:
            filtered_property = [getattr(x, property_name) for x in self.get_queryset()]
            payload = dict(Counter(filtered_property))
        else:
            payload = {"LETTERS_PRIV": 7280, "BIBLE": 22329, None: 2, "ROMANCE": 12661, "HANDBOOK_OTHER": 8672, "EDUC_TREATISE": 7465, "RELIG_TREATISE": 68217, "PHILOSOPHY/FICTION": 3252, "DRAMA_COMEDY": 5285, "HOMILY_POETRY": 8573, "BIOGRAPHY_LIFE_OF_SAINT": 5372, "HANDBOOK_ASTRO": 1885, "DIARY_PRIV": 9437, "BIOGRAPHY_OTHER": 3518, "BIOGRAPHY_AUTO": 2008, "FICTION": 8793, "RULE": 5896, "LAW": 6392, "SCIENCE_OTHER": 5036, "SCIENCE_MEDICINE": 2801, "RELIG_TRREATISE": 2638, "TRAVELOGUE": 16486, "PROCEEDINGS_TRIAL": 7961, "LETTERS_NON-PRIV": 4319, "PHILOSOPHY": 7354, "HOMILY": 16424, "SERMON": 32217, "HISTORY": 47885, "HANDBOOK_MEDICINE": 1637}

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
        return context
