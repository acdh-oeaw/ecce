from django_tables2 import SingleTableView, RequestConfig
from tokens.models import *
from .filters import *
from .forms import *
from .tables import *
from django.shortcuts import render, render_to_response
from django.http import HttpResponse
import pandas as pd


class GenericListView(SingleTableView):
    filter_class = None
    formhelper_class = None
    context_filter_name = 'filter'
    paginate_by = 25
    template_name = 'browsing/generic_list.html'

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
        context['docstring'] = "{}".format(self.model.__doc__)
        if self.model.__name__.endswith('s'):
            context['class_name'] = "{}".format(self.model.__name__)
        else:
            context['class_name'] = "{}s".format(self.model.__name__)
        return context


class TokenListView(GenericListView):
    model = Token
    table_class = TokenTable
    filter_class = TokenListFilter
    formhelper_class = TokenFilterFormHelper
    init_columns = ['legacy_id', 'plain_word', 'pos', 'lemma', 'cluster',
                    'label', 'date']

    def get_all_cols(self):
        all_cols = list(self.table_class.base_columns.keys())
        return all_cols

    def get_context_data(self, **kwargs):
        context = super(TokenListView, self).get_context_data()
        context[self.context_filter_name] = self.filter
        togglable_colums = [x for x in self.get_all_cols() if x not in self.init_columns]
        context['togglable_colums'] = togglable_colums
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
    filter_class = DateListFilter
    formhelper_class = GenericFilterFormHelper


class CorpusListView(GenericListView):
    model = Corpus
    table_class = CorpusTable
    filter_class = CorpusListFilter
    formhelper_class = GenericFilterFormHelper


class TextListView(GenericListView):
    model = Text
    table_class = TextTable
    filter_class = TextListFilter
    formhelper_class = GenericFilterFormHelper


class ConsonantListView(GenericListView):
    model = Consonant
    table_class = ConsonantTable
    filter_class = ConsonantListFilter
    formhelper_class = GenericFilterFormHelper


class ClusterListView(GenericListView):
    model = Cluster
    table_class = ClusterTable
    filter_class = ClusterListFilter
    formhelper_class = GenericFilterFormHelper


class TokenLabelListView(GenericListView):
    model = TokenLabel
    table_class = TokenLabelTable
    filter_class = TokenLabelListFilter
    formhelper_class = GenericFilterFormHelper


class SchwaPresentListView(GenericListView):
    model = SchwaPresent
    table_class = SchwaPresentTable
    filter_class = SchwaPresentListFilter
    formhelper_class = GenericFilterFormHelper


class OnSetListView(GenericListView):
    model = OnSet
    table_class = OnSetTable
    filter_class = OnSetListFilter
    formhelper_class = GenericFilterFormHelper


class TokenCustomView(GenericListView):
    model = Token
    table_class = TokenTable
    filter_class = TokenCustomFilter
    formhelper_class = TokenCustomFilterFormHelper
    template_name = 'browsing/browse_tokens_custom.html'
    init_columns = ['legacy_id', 'plain_word', 'pos', 'lemma', 'cluster',
                    'label', 'date']

    def get_all_cols(self):
        all_cols = list(self.table_class.base_columns.keys())
        return all_cols

    def get_context_data(self, **kwargs):
        context = super(TokenCustomView, self).get_context_data()
        context[self.context_filter_name] = self.filter
        togglable_colums = [x for x in self.get_all_cols() if x not in self.init_columns]
        context['togglable_colums'] = togglable_colums
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


class FrequenciesView(GenericListView):
    model = Token
    filter_class = TokenCustomFilter
    table_class = FrequenciesTable
    formhelper_class = TokenCustomFilterFormHelper
    template_name = 'browsing/browse_frequencies.html'

    def get_context_data(self, **kwargs):
        context = super(FrequenciesView, self).get_context_data()
        tokens_grouped = pd.DataFrame(list(self.get_queryset().values_list(
            'legacy_id',
            'text_source__mean_date__semicentury',
            'text_source__mean_date__pr_cc_final_V',
            'text_source__mean_date__pr_cc_both',
            'text_source__mean_date__pr_cc_no'
        ),), columns = ["legacy_id", "semicentury", "pr_cc_final_V", "pr_cc_both", "pr_cc_no"]).groupby('semicentury')
        
        norm_prob = tokens_grouped['pr_cc_final_V'].sum()
        norm_full = tokens_grouped['pr_cc_both'].sum()
        norm_no = tokens_grouped['pr_cc_no'].sum()
        raw_count = tokens_grouped.size().rename('tokens count')
        out = pd.concat([raw_count, norm_prob, norm_full, norm_no], axis=1)
        #to remove trailing zeroes in all columns  - convert to string .astype(str)
        out.loc["Total"] = [x.sum() for x in [raw_count, norm_prob , norm_full , norm_no]]
        context["freq_table"] = out.to_html(classes="freq-table table table-responsive")
        #context["freq_table"] = out.to_json()
        return context