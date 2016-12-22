from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
from .models import Date, Corpus, Text, Consonant
from .forms import DateForm, CorpusForm, TextForm, ConsonantForm


class DateDetailView(DetailView):

    model = Date
    template_name = 'tokens/date_detail.html'


class DateListView(ListView):

    model = Date
    template_name = 'tokens/date_list.html'


class DateCreate(CreateView):

    model = Date
    template_name = 'tokens/date_create.html'
    form_class = DateForm


class DateUpdate(UpdateView):

    model = Date
    form_class = DateForm
    template_name = 'tokens/date_create.html'


class CorpusDetailView(DetailView):

    model = Corpus
    template_name = 'tokens/corpus_detail.html'


class CorpusListView(ListView):

    model = Corpus
    template_name = 'tokens/corpus_list.html'


class CorpusCreate(CreateView):

    model = Corpus
    template_name = 'tokens/corpus_create.html'
    form_class = CorpusForm


class CorpusUpdate(UpdateView):

    model = Corpus
    form_class = CorpusForm
    template_name = 'tokens/corpus_create.html'


class TextDetailView(DetailView):

    model = Text
    template_name = 'tokens/text_detail.html'


class TextListView(ListView):

    model = Text
    template_name = 'tokens/text_list.html'


class TextCreate(CreateView):

    model = Text
    template_name = 'tokens/text_create.html'
    form_class = TextForm


class TextUpdate(UpdateView):

    model = Text
    form_class = TextForm
    template_name = 'tokens/text_create.html'


class ConsonantDetailView(DetailView):

    model = Consonant
    template_name = 'tokens/consonant_detail.html'


class ConsonantListView(ListView):

    model = Consonant
    template_name = 'tokens/consonant_list.html'


class ConsonantCreate(CreateView):

    model = Consonant
    template_name = 'tokens/consonant_create.html'
    form_class = ConsonantForm


class ConsonantUpdate(UpdateView):

    model = Consonant
    form_class = ConsonantForm
    template_name = 'tokens/consonant_create.html'
