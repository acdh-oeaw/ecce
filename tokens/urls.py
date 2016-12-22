from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^date/$', views.DateListView.as_view(),
        name='date_list'),
    url(
        r'^date/(?P<pk>[0-9]+)$', views.DateDetailView.as_view(),
        name='date_detail'),
    url(
        r'^date/create/$', views.DateCreate.as_view(),
        name='date_create'),
    url(
        r'^date/update/(?P<pk>[0-9]+)$', views.DateUpdate.as_view(),
        name='date_update'),
    url(r'^corpus/$', views.CorpusListView.as_view(),
        name='corpus_list'),
    url(
        r'^corpus/(?P<pk>[0-9]+)$', views.CorpusDetailView.as_view(),
        name='corpus_detail'),
    url(
        r'^corpus/create/$', views.CorpusCreate.as_view(),
        name='corpus_create'),
    url(
        r'^corpus/update/(?P<pk>[0-9]+)$', views.CorpusUpdate.as_view(),
        name='corpus_update'),
    url(r'^text/$', views.TextListView.as_view(),
        name='text_list'),
    url(
        r'^text/(?P<pk>[0-9]+)$', views.TextDetailView.as_view(),
        name='text_detail'),
    url(
        r'^text/create/$', views.TextCreate.as_view(),
        name='text_create'),
    url(
        r'^text/update/(?P<pk>[0-9]+)$', views.TextUpdate.as_view(),
        name='text_update'),
    url(r'^consonant/$', views.ConsonantListView.as_view(),
        name='consonant_list'),
    url(
        r'^consonant/(?P<pk>[0-9]+)$', views.ConsonantDetailView.as_view(),
        name='consonant_detail'),
    url(
        r'^consonant/create/$', views.ConsonantCreate.as_view(),
        name='consonant_create'),
    url(
        r'^consonant/update/(?P<pk>[0-9]+)$', views.ConsonantUpdate.as_view(),
        name='consonant_update'),
]
