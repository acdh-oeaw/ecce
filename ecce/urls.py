from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from vocabs.api_views import *
from tokens.api_views import *


router = routers.DefaultRouter()
router.register(r'skoslabels', SkosLabelViewSet)
router.register(r'skosnamespaces', SkosNamespaceViewSet)
router.register(r'skosconceptschemes', SkosConceptSchemeViewSet)
router.register(r'skosconcepts', SkosConceptViewSet)
router.register(r'lemma', LemmaViewSet)
router.register(r'date', DateViewSet)
router.register(r'corpus', CorpusViewSet)
router.register(r'text', TextViewSet)
router.register(r'consonant', ConsonantViewSet)
router.register(r'cluster', ClusterViewSet)
router.register(r'tokenlabel', TokenLabelViewSet)
router.register(r'schwapresent', SchwaPresentViewSet)
router.register(r'onset', OnSetViewSet)
router.register(r'token', TokenViewSet)


urlpatterns = [
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', admin.site.urls),
    url(r'^', include('webpage.urls', namespace='webpage')),
    url(r'^vocabs/', include('vocabs.urls', namespace='vocabs')),
    url(r'^tokens/', include('tokens.urls', namespace='tokens')),
    url(r'^charts/', include('charts.urls', namespace='charts')),
    url(r'^browsing/', include('browsing.urls', namespace='browsing')),
    url(r'^autocomplete/', include('tokens.dal_urls', namespace='dal_ac')),
    url(r'^datamodel/', include('django_spaghetti.urls', namespace='datamodel')),
]
