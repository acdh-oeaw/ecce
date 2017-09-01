from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^chartselector/$', views.ChartSelector.as_view(), name='chart_selector'),
    url(r'^barcharts/(?P<property>[\w\-]+)/$', views.DynChartView.as_view(), name='dynchart'),
]
