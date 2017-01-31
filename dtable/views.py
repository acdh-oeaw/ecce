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
        filtered_objects = NormTokenListFilter(
            self.request.GET, queryset=NormToken.objects.all()
        )

        context['filtered_objects'] = filtered_objects[1:20]
        return context
