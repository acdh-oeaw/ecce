from django.conf.urls import url
from . import dal_views
from .models import Cluster

urlpatterns = [
	url(
        r'^cluster-ac/$', dal_views.ClusterAC.as_view(
            model=Cluster), name='cluster-ac',
    ),
]