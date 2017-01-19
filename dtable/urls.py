from django.conf.urls import url

from .views import TextDtableJson, TextDtable

urlpatterns = [
    url(r'^text-data/$', TextDtableJson.as_view(), name="text-data"),
    url(r'^text-dtable/$', TextDtable.as_view(), name="text-dtable"),
]
