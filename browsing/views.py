from django_tables2 import SingleTableView, RequestConfig
from tokens.models import *
from dtable.models import NormToken
from .filters import *
from .forms import *
from .tables import *


class GenericListView(SingleTableView):
    filter_class = None
    formhelper_class = None
    context_filter_name = 'filter'
    paginate_by = 25

    def get_queryset(self, **kwargs):
        qs = super(GenericListView, self).get_queryset()
        self.filter = self.filter_class(self.request.GET, queryset=qs)
        self.filter.form.helper = self.formhelper_class()
        return self.filter.qs

    def get_table(self, **kwargs):
        table = super(GenericListView, self).get_table()
        RequestConfig(self.request, paginate={
            'page': 1, 'per_page': self.paginate_by}).configure(table)
        return table

    def get_context_data(self, **kwargs):
        context = super(GenericListView, self).get_context_data()
        context[self.context_filter_name] = self.filter
        return context


class AllInOneView(GenericListView):
    model = NormToken
    table_class = NormTokenTable
    template_name = 'browsing/normtoken.html'
    filter_class = NormTokenListFilter
    formhelper_class = NormTokenFilterFormHelper

    def get_context_data(self, **kwargs):
        context = super(GenericListView, self).get_context_data()
        context[self.context_filter_name] = self.filter
        init_columns = [
            'plain_word', 'pos', 'cluster_consonant', 'medial_suffix', 'final_suffix'
        ]
        all_columns = [f.name for f in self.model._meta.get_fields()]
        toogable_colums = list(set(all_columns) - set(init_columns))
        context['toogable_colums'] = toogable_colums
        return context


class TokenListView(GenericListView):
    model = Token
    table_class = TokenTable
    template_name = 'browsing/token_list_generic.html'
    filter_class = TokenListFilter
    formhelper_class = GenericFilterFormHelper
    init_columns = ['plain_word']

    def get_all_cols(self):
        all_cols = list(self.table_class.base_columns.keys())
        return all_cols

    def get_context_data(self, **kwargs):
        context = super(TokenListView, self).get_context_data()
        context[self.context_filter_name] = self.filter
        toogable_colums = [x for x in self.get_all_cols() if x not in self.init_columns]
        context['toogable_colums'] = toogable_colums
        return context

    def get_table(self, **kwargs):
        table = super(GenericListView, self).get_table()
        RequestConfig(self.request, paginate={
            'page': 1, 'per_page': self.paginate_by}).configure(table)
        default_cols = self.init_columns
        all_cols = self.get_all_cols()
        selected_cols = self.request.GET.getlist("columns") + default_cols
        exclude_vals = [x for x in all_cols if x not in selected_cols]
        table.exclude = exclude_vals
        return table


class DateListView(GenericListView):
    model = Date
    table_class = DateTable
    template_name = 'browsing/date_list_generic.html'
    filter_class = DateListFilter
    formhelper_class = GenericFilterFormHelper


class CorpusListView(GenericListView):
    model = Corpus
    table_class = CorpusTable
    template_name = 'browsing/corpus_list_generic.html'
    filter_class = CorpusListFilter
    formhelper_class = GenericFilterFormHelper


class TextListView(GenericListView):
    model = Text
    table_class = TextTable
    template_name = 'browsing/text_list_generic.html'
    filter_class = TextListFilter
    formhelper_class = GenericFilterFormHelper


class ConsonantListView(GenericListView):
    model = Consonant
    table_class = ConsonantTable
    template_name = 'browsing/consonant_list_generic.html'
    filter_class = ConsonantListFilter
    formhelper_class = GenericFilterFormHelper


class ClusterListView(GenericListView):
    model = Cluster
    table_class = ClusterTable
    template_name = 'browsing/cluster_list_generic.html'
    filter_class = ClusterListFilter
    formhelper_class = GenericFilterFormHelper


class TokenLabelListView(GenericListView):
    model = TokenLabel
    table_class = TokenLabelTable
    template_name = 'browsing/tokenlabel_list_generic.html'
    filter_class = TokenLabelListFilter
    formhelper_class = GenericFilterFormHelper


class SchwaPresentListView(GenericListView):
    model = SchwaPresent
    table_class = SchwaPresentTable
    template_name = 'browsing/schwapresent_list_generic.html'
    filter_class = SchwaPresentListFilter
    formhelper_class = GenericFilterFormHelper


class OnSetListView(GenericListView):
    model = OnSet
    table_class = OnSetTable
    template_name = 'browsing/onset_list_generic.html'
    filter_class = OnSetListFilter
    formhelper_class = GenericFilterFormHelper
