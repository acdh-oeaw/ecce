from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'tokens/$', views.TokenListView.as_view(), name='browse_tokens'),
]