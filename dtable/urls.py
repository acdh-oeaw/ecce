from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^text-data/$', views.TextDtableJson.as_view(), name="text-data"),
    url(r'^text-dtable/$', views.TextDtable.as_view(), name="text-dtable"),
    url(r'^normtoken-data/$', views.NormTokenDtableJson.as_view(), name="normtoken-data"),
    url(r'^normtoken-dtable/$', views.NormTokenDtable.as_view(), name="normtoken-dtable")
]
