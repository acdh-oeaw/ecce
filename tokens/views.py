from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
from .models import *
from .forms import *


class LemmaDetailView(DetailView):

    model = Lemma
    template_name = 'tokens/lemma_detail.html'


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


class ClusterDetailView(DetailView):

    model = Cluster
    template_name = 'tokens/cluster_detail.html'


class ClusterListView(ListView):

    model = Cluster
    template_name = 'tokens/cluster_list.html'


class ClusterCreate(CreateView):

    model = Cluster
    template_name = 'tokens/cluster_create.html'
    form_class = ClusterForm


class ClusterUpdate(UpdateView):

    model = Cluster
    form_class = ClusterForm
    template_name = 'tokens/cluster_create.html'


class TokenLabelDetailView(DetailView):

    model = TokenLabel
    template_name = 'tokens/tokenlabel_detail.html'


class TokenLabelListView(ListView):

    model = TokenLabel
    template_name = 'tokens/tokenlabel_list.html'


class TokenLabelCreate(CreateView):

    model = TokenLabel
    template_name = 'tokens/tokenlabel_create.html'
    form_class = TokenLabelForm


class TokenLabelUpdate(UpdateView):

    model = TokenLabel
    form_class = TokenLabelForm
    template_name = 'tokens/tokenlabel_create.html'


class SchwaPresentDetailView(DetailView):

    model = SchwaPresent
    template_name = 'tokens/schwapresent_detail.html'


class SchwaPresentListView(ListView):

    model = SchwaPresent
    template_name = 'tokens/schwapresent_list.html'


class SchwaPresentCreate(CreateView):

    model = SchwaPresent
    template_name = 'tokens/schwapresent_create.html'
    form_class = SchwaPresentForm


class SchwaPresentUpdate(UpdateView):

    model = SchwaPresent
    form_class = SchwaPresentForm
    template_name = 'tokens/schwapresent_create.html'


class OnSetDetailView(DetailView):

    model = OnSet
    template_name = 'tokens/onset_detail.html'


class OnSetListView(ListView):

    model = OnSet
    template_name = 'tokens/onset_list.html'


class OnSetCreate(CreateView):

    model = OnSet
    template_name = 'tokens/onset_create.html'
    form_class = OnSetForm


class OnSetUpdate(UpdateView):

    model = OnSet
    form_class = OnSetForm
    template_name = 'tokens/onset_create.html'


class TokenDetailView(DetailView):

    model = Token
    template_name = 'tokens/token_detail.html'


class TokenListView(ListView):

    model = Token
    template_name = 'tokens/token_list.html'


class TokenCreate(CreateView):

    model = Token
    template_name = 'tokens/token_create.html'
    form_class = TokenForm


class TokenUpdate(UpdateView):

    model = Token
    form_class = TokenForm
    template_name = 'tokens/token_create.html'
