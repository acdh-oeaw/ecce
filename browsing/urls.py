from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'tokens/$', views.TokenListView.as_view(), name='browse_tokens'),
    url(r'dates/$', views.DateListView.as_view(), name='browse_dates'),
    url(r'corpora/$', views.CorpusListView.as_view(), name='browse_corpora'),
    url(r'texts/$', views.TextListView.as_view(), name='browse_texts'),
    url(r'consonants/$', views.ConsonantListView.as_view(), name='browse_consonants'),
    url(r'clusters/$', views.ClusterListView.as_view(), name='browse_clusters'),
    url(r'tokenlabels/$', views.TokenLabelListView.as_view(), name='browse_tokenlabels'),
    url(r'schwapresents/$', views.SchwaPresentListView.as_view(), name='browse_schwapresents'),
    url(r'onsets/$', views.OnSetListView.as_view(), name='browse_onsets'),
    url(r'tokens-custom/$', views.TokenCustomView.as_view(), name='browse_tokens_custom'),
]