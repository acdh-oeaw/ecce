import django_filters
from .models import *
from vocabs.models import SkosConcept
from django_filters.rest_framework import FilterSet


class LemmaRestFilter(django_filters.rest_framework.FilterSet):

    class Meta:
        model = Lemma
        fields = "__all__"
        

class DateRestFilter(django_filters.rest_framework.FilterSet):

    class Meta:
        model = Date
        fields = "__all__"


class CorpusRestFilter(django_filters.rest_framework.FilterSet):

    class Meta:
        model = Corpus
        fields = "__all__"


class TextRestFilter(django_filters.rest_framework.FilterSet):

    class Meta:
        model = Text
        fields = "__all__"


class ConsonantRestFilter(django_filters.rest_framework.FilterSet):

    class Meta:
        model = Consonant
        fields = "__all__"


class ClusterRestFilter(django_filters.rest_framework.FilterSet):

    class Meta:
        model = Cluster
        fields = "__all__"


class TokenLabelRestFilter(django_filters.rest_framework.FilterSet):

    class Meta:
        model = TokenLabel
        fields = "__all__"


class SchwaPresentRestFilter(django_filters.rest_framework.FilterSet):

    class Meta:
        model = SchwaPresent
        fields = "__all__"


class OnSetRestFilter(django_filters.rest_framework.FilterSet):

    class Meta:
        model = OnSet
        fields = "__all__"