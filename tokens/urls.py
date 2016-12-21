from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^date/$', views.DateListView.as_view(), name='date_list'),
    url(
        r'^date/(?P<pk>[0-9]+)$', views.DateDetailView.as_view(),
        name='date_detail'),
    url(
        r'^date/create/$', views.DateCreate.as_view(),
        name='date_create'),
    url(
        r'^date/update/(?P<pk>[0-9]+)$', views.DateUpdate.as_view(),
        name='date_update'),
]
