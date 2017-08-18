from django import template
from webpage.metadata import PROJECT_METADATA as PM
from tokens.models import *
import datetime

register = template.Library()


@register.simple_tag
def projects_metadata(key):
    return PM[key]

@register.simple_tag
def tokens_count():
	tokens_count = Token.objects.count()
	return tokens_count

@register.simple_tag
def dates_count():
	dates_count = Date.objects.count()
	return dates_count
	
@register.simple_tag
def corpora_count():
	corpora_count = Corpus.objects.count()
	return corpora_count

@register.simple_tag
def texts_count():
	texts_count = Text.objects.count()
	return texts_count

@register.simple_tag
def consonants_count():
	consonants_count = Consonant.objects.count()
	return consonants_count

@register.simple_tag
def clusters_count():
	clusters_count = Cluster.objects.count()
	return clusters_count

@register.simple_tag
def tokenlabels_count():
	tokenlabels_count = TokenLabel.objects.count()
	return tokenlabels_count

@register.simple_tag
def schwapresents_count():
	schwapresents_count = SchwaPresent.objects.count()
	return schwapresents_count

@register.simple_tag
def onsets_count():
	onsets_count = OnSet.objects.count()
	return onsets_count