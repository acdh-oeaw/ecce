from django.db.models import Q
from django.views.generic import TemplateView
from django_datatables_view.base_datatable_view import BaseDatatableView
from .models import NormToken
from tokens.models import Text


class TextDtableJson(BaseDatatableView):
    model = Text
    columns = ['text', 'date', 'genre', 'corpus', 'dialect']
    order_columns = ['text', 'date', 'genre', 'corpus', 'dialect']
    max_display_length = 200

    def filter_queryset(self, qs):
        search = self.request.GET.get('search[value]', None)
        if search:
            q = (
                Q(text__istartswith=search) | Q(genre__pref_label__startswith=search) |
                Q(corpus__name__istartswith=search)
            )
            qs = qs.filter(q)
        return qs


class TextDtable(TemplateView):
    template_name = "dtable/text_dtable.html"


fields = [f.name for f in NormToken._meta.get_fields() if f.name != 'label_description']


class NormTokenDtableJson(BaseDatatableView):
    model = NormToken
    columns = fields
    order_columns = fields
    max_display_length = 100


class NormTokenDtable(TemplateView):
    template_name = "dtable/normtoken_dtable.html"

    def get_context_data(self, **kwargs):
        context = super(NormTokenDtable, self).get_context_data(**kwargs)
        context['th_headers'] = fields
        return context
