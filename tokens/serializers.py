# -*- coding: utf-8 -*-
from rest_framework import serializers
from .models import *
from vocabs.models import *
from vocabs.serializers import *


class LemmaSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Lemma
		fields = '__all__'


class DateSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Date
		fields = '__all__'


class CorpusSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Corpus
		fields = '__all__'


class TextSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Text
		fields = '__all__'


class ConsonantSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Consonant
		fields = '__all__'


class ClusterSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Cluster
		fields = '__all__'


class TokenLabelSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = TokenLabel
		fields = '__all__'


class SchwaPresentSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = SchwaPresent
		fields = '__all__'


class OnSetSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = OnSet
		fields = '__all__'


class TokenSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Token
		fields = '__all__'