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
    url(r'^cluster/$', views.ClusterListView.as_view(),
        name='cluster_list'),
    url(
        r'^cluster/(?P<pk>[0-9]+)$', views.ClusterDetailView.as_view(),
        name='cluster_detail'),
    url(
        r'^cluster/create/$', views.ClusterCreate.as_view(),
        name='cluster_create'),
    url(
        r'^cluster/update/(?P<pk>[0-9]+)$', views.ClusterUpdate.as_view(),
        name='cluster_update'),
    url(r'^tokenlabel/$', views.TokenLabelListView.as_view(),
        name='tokenlabel_list'),
    url(
        r'^tokenlabel/(?P<pk>[0-9]+)$', views.TokenLabelDetailView.as_view(),
        name='tokenlabel_detail'),
    url(
        r'^tokenlabel/create/$', views.TokenLabelCreate.as_view(),
        name='tokenlabel_create'),
    url(
        r'^tokenlabel/update/(?P<pk>[0-9]+)$', views.TokenLabelUpdate.as_view(),
        name='tokenlabel_update'),
    url(r'^schwapresent/$', views.SchwaPresentListView.as_view(),
        name='schwapresent_list'),
    url(
        r'^schwapresent/(?P<pk>[0-9]+)$', views.SchwaPresentDetailView.as_view(),
        name='schwapresent_detail'),
    url(
        r'^schwapresent/create/$', views.SchwaPresentCreate.as_view(),
        name='schwapresent_create'),
    url(
        r'^schwapresent/update/(?P<pk>[0-9]+)$', views.SchwaPresentUpdate.as_view(),
        name='schwapresent_update'),
    url(r'^onset/$', views.OnSetListView.as_view(),
        name='onset_list'),
    url(
        r'^onset/(?P<pk>[0-9]+)$', views.OnSetDetailView.as_view(),
        name='onset_detail'),
    url(
        r'^onset/create/$', views.OnSetCreate.as_view(),
        name='onset_create'),
    url(
        r'^onset/update/(?P<pk>[0-9]+)$', views.OnSetUpdate.as_view(),
        name='onset_update'),
    url(r'^token/$', views.TokenListView.as_view(),
        name='token_list'),
    url(
        r'^token/(?P<pk>[0-9]+)$', views.TokenDetailView.as_view(),
        name='token_detail'),
    url(
        r'^token/create/$', views.TokenCreate.as_view(),
        name='token_create'),
    url(
        r'^token/update/(?P<pk>[0-9]+)$', views.TokenUpdate.as_view(),
        name='token_update'),
    url(
        r'^lemma/(?P<pk>[0-9]+)$', views.LemmaDetailView.as_view(),
        name='lemma_detail'),
]
