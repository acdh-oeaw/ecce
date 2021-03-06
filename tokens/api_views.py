from rest_framework import viewsets, generics, pagination, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
import django_filters
from .models import *
from .serializers import *
from .api_filters import *
from django_filters.rest_framework import FilterSet


class CustomPagination(pagination.PageNumberPagination):
    page_size = 25
    page_size_query_param = 'page_size'
    max_page_size = 10000

    def get_paginated_response(self, data):
        return Response({
            'links': {
               'next': self.get_next_link(),
               'previous': self.get_previous_link()
            },
            'count': self.page.paginator.count,
            'total_pages': self.page.paginator.num_pages,
            'results': data
        })


class LemmaViewSet(viewsets.ModelViewSet):
    queryset = Lemma.objects.all()
    serializer_class = LemmaSerializer
    pagination_class = CustomPagination
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter, )
    filter_class = LemmaRestFilter
    ordering_fields = '__all__'


class DateViewSet(viewsets.ModelViewSet):
    queryset = Date.objects.all()
    serializer_class = DateSerializer
    pagination_class = CustomPagination
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter, )
    filter_class = DateRestFilter
    ordering_fields = '__all__'


class CorpusViewSet(viewsets.ModelViewSet):
    queryset = Corpus.objects.all()
    serializer_class = CorpusSerializer
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter, )
    filter_class = CorpusRestFilter
    ordering_fields = '__all__'


class TextViewSet(viewsets.ModelViewSet):
    queryset = Text.objects.all()
    serializer_class = TextSerializer
    pagination_class = CustomPagination
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter, )
    filter_class = TextRestFilter
    ordering_fields = '__all__'


class ConsonantViewSet(viewsets.ModelViewSet):
    queryset = Consonant.objects.all()
    serializer_class = ConsonantSerializer
    pagination_class = CustomPagination
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter, )
    filter_class = ConsonantRestFilter
    ordering_fields = '__all__'


class ClusterViewSet(viewsets.ModelViewSet):
    queryset = Cluster.objects.all()
    serializer_class = ClusterSerializer
    pagination_class = CustomPagination
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter, )
    filter_class = ClusterRestFilter
    ordering_fields = '__all__'


class TokenLabelViewSet(viewsets.ModelViewSet):
    queryset = TokenLabel.objects.all()
    serializer_class = TokenLabelSerializer
    pagination_class = CustomPagination
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter, )
    filter_class = TokenLabelRestFilter
    ordering_fields = '__all__'


class SchwaPresentViewSet(viewsets.ModelViewSet):
    queryset = SchwaPresent.objects.all()
    serializer_class = SchwaPresentSerializer
    pagination_class = CustomPagination
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter, )
    filter_class = SchwaPresentRestFilter
    ordering_fields = '__all__'


class OnSetViewSet(viewsets.ModelViewSet):
    queryset = OnSet.objects.all()
    serializer_class = OnSetSerializer
    pagination_class = CustomPagination
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter, )
    filter_class = OnSetRestFilter
    ordering_fields = '__all__'


class TokenViewSet(viewsets.ModelViewSet):
    queryset = Token.objects.all()
    serializer_class = TokenSerializer
    pagination_class = CustomPagination
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter, )
    filter_class = TokenRestFilter
    ordering_fields = '__all__'

    #https://github.com/encode/django-rest-framework/issues/3636