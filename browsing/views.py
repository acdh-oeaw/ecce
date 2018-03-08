from django_tables2 import SingleTableView, RequestConfig
from tokens.models import *
from .filters import *
from .forms import *
from .tables import *
from django.shortcuts import render, render_to_response
from django.http import HttpResponse
import pandas as pd
import csv
import re
import time
import datetime
import requests


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
            'weight',
            'weight_norm',
            'weight_not_norm'
        ),), columns = ["legacy_id", "Semicentury", "Weighted", "Normalized and weighted", "Normalized"]).groupby('Semicentury')

        norm_prob = tokens_grouped['Normalized and weighted'].sum()
        norm_full = tokens_grouped['Normalized'].sum()
        norm_no = tokens_grouped['Weighted'].sum()
        raw_count = tokens_grouped.size().rename('Tokens')
        out = pd.concat([raw_count, norm_no, norm_prob, norm_full], axis=1)
        #to remove trailing zeroes in all columns  - convert to string .astype(str)
        out.loc["Total"] = [x.sum() for x in [raw_count, norm_no, norm_prob, norm_full]]
        context["freq_table"] = out.to_html(classes="freq-table table table-responsive")
        #context["freq_table"] = out.to_json()
        return context


class FrequenciesDownloadView(GenericListView):
    model = Token
    filter_class = TokenCustomFilter
    table_class = FrequenciesTable
    formhelper_class = TokenCustomFilterFormHelper
    template_name = 'browsing/browse_frequencies.html'


    def render_to_response(self, context, **kwargs):
        timestamp = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d-%H-%M-%S')
        response = HttpResponse(content_type='text/csv')
        filename = "ecce_export_{}".format(timestamp)
        response['Content-Disposition'] = 'attachment; filename="{}.csv"'.format(filename)
        tokens_grouped = pd.DataFrame(list(self.get_queryset().values_list(
            'legacy_id',
            'text_source__mean_date__semicentury',
            'weight',
            'weight_norm',
            'weight_not_norm'
        ),), columns = ["legacy_id", "Semicentury", "Weighted", "Normalized and weighted", "Normalized"]).groupby('Semicentury')
        semicentury = tokens_grouped['Semicentury'].unique().astype(int)
        norm_prob = tokens_grouped['Normalized and weighted'].sum()
        norm_full = tokens_grouped['Normalized'].sum()
        norm_no = tokens_grouped['Weighted'].sum()
        raw_count = tokens_grouped.size().rename('Tokens')
        out = pd.concat([semicentury, raw_count, norm_prob, norm_full, norm_no], axis=1)
        out.loc["Total"] = ["Total", sum(raw_count), sum(norm_prob), sum(norm_full),  sum(norm_no)]
        #out.loc["Total"] = [x.sum() for x in [semicentury, raw_count, norm_prob , norm_full , norm_no]]
        out.to_csv(path_or_buf=response, sep=',', index=False, decimal=".")
        return response


class TokenDownloadView(GenericListView):
    model = Token
    table_class = TokenTable
    filter_class = TokenCustomFilter
    formhelper_class = TokenCustomFilterFormHelper
    template_name = 'browsing/browse_tokens_custom.html'

    def render_to_response(self, context, **kwargs):
        timestamp = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d-%H-%M-%S')
        response = HttpResponse(content_type='text/csv')
        filename = "ecce_export_{}".format(timestamp)
        response['Content-Disposition'] = 'attachment; filename="{}.csv"'.format(filename)
        writer = csv.writer(response, delimiter=",")
        writer.writerow([
            'Identifier', 'Plain Word',
            'Part Of Speech', 'Word Lemma',
            'Cluster', 'Morphological Status',
            'Date'
            ]
        )
        for obj in self.get_queryset()[:1000]:
            writer.writerow([
                obj.legacy_id, obj.plain_word,
                obj.pos,
                obj.lemma,
                obj.cluster,
                obj.label,
                obj.text_source.mean_date.dates
                ])
        return response
