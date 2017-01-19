from django.conf.urls import url
from . import dal_views
from .models import Cluster, Token

urlpatterns = [
    url(
        r'^cluster-ac/$', dal_views.ClusterAC.as_view(model=Cluster),
        name='cluster-ac',
    ),
    url(
        r'^tokenlabel-ac/$', dal_views.ClusterAC.as_view(model=Cluster),
        name='tokenlabel-ac',
    ),
    url(
        r'^token-ac/$', dal_views.TokenAC.as_view(), name='token-ac',
    ),
    url(
        r'^tokenM-ac/$', dal_views.TokenModelAC.as_view(model=Token), name='tokenM-ac',
    ),
]
