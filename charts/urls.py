from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^barcharts/$', views.barcharts_view, name='bar_charts'),
    url(r'^piecharts/$', views.piecharts_view, name='pie_charts'),
    url(r'^linecharts/$', views.linecharts_view, name='line_charts'),
    url(r'^testjson/$', views.test_json, name='test_json'),
    url(r'^testjsonpie/$', views.test_json_pie, name='test_json_pie'),
    url(r'^data-token-per-genre/$', views.tokens_per_genre, name='data-token-per-genre'),
    url(r'^data-token-per-genre-static/$', views.tokens_per_genre_static, name='data-token-per-genre-static'),
    url(r'^data-token-per-date/$', views.tokens_per_date, name='data-token-per-date'),
]
