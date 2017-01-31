from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'dynchart/$', views.DynChartView.as_view(), name='dynchart'),
]
