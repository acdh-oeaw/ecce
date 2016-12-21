from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
from .models import Date
from .forms import DateForm


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
