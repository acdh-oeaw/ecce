from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.StartView.as_view(), name="start"),
    url(r'^project-info/$', views.project_info, name='project_info'),
    url(r'^imprint/$', views.ImprintView.as_view(), name='imprint'),
    url(r'^about/$', views.AboutView.as_view(), name='about'),
    url(r'^user-manual/$', views.ManualView.as_view(), name='manual'),
    url(r'^acknowledgements/$', views.AcknowledgementsView.as_view(), name='acknowledgements'),
    url(r'^accounts/login/$', views.user_login, name='user_login'),
    url(r'^logout/$', views.user_logout, name='user_logout'),
]
