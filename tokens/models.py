from django.db import models
from vocabs.models import SkosConcept


class Date(models.Model):
    dates = models.IntegerField(primary_key=True)
    decade = models.IntegerField(blank=True, null=True)
    semicentury = models.IntegerField(blank=True, null=True)
    century = models.IntegerField(blank=True, null=True)
    pr_cc_checekd = models.FloatField(blank=True, null=True)
    pr_cc_final = models.FloatField(blank=True, null=True)
    pr_cc_final_V = models.FloatField(blank=True, null=True)
    pr_cc_both = models.FloatField(blank=True, null=True)
    pr_cc_no = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return "{}".format(self.dates)


class Corpus(models.Model):
    name = models.CharField(blank=True, null=True, max_length=100)

    def __str__(self):
        return "{}".format(self.name)


class Text(models.Model):
    text = models.CharField(blank=True, null=True, max_length=100)
    date = models.CharField(blank=True, null=True, max_length=100)
    genre = models.ForeignKey(SkosConcept, blank=True, null=True, related_name="skos_genre")
    corpus = models.ForeignKey(Corpus, blank=True, null=True, related_name="text_corpus")
    lower = models.IntegerField(blank=True, null=True)
    mean_date = models.ForeignKey(Date, blank=True, null=True)
    size = models.IntegerField(blank=True, null=True)
    dialect = models.ForeignKey(SkosConcept, blank=True, null=True, related_name="skos_dialect")

    def __str__(self):
        return "{}".format(self.text)


class Consonant(models.Model):
    consonant = models.CharField(blank=True, null=True, max_length=1)
    art_manner = models.ForeignKey(
        SkosConcept, blank=True, null=True, related_name="skos_art_manner")
    art_place = models.ForeignKey(
        SkosConcept, blank=True, null=True, related_name="skos_art_place")
    voice = models.ForeignKey(
        SkosConcept, blank=True, null=True, related_name="skos_voice")
    airflow = models.ForeignKey(
        SkosConcept, blank=True, null=True, related_name="skos_airflow")
    sonority = models.IntegerField(blank=True, null=True)
    transcription = models.CharField(blank=True, null=True, max_length=1)
    place_ord = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return "{}".format(self.consonant)


class Cluster(models.Model):
    first_consonant = models.ForeignKey(
        Consonant, blank=True, null=True, related_name="consonant_first")
    second_consonant = models.ForeignKey(
        Consonant, blank=True, null=True, related_name="consonant_second")
    third_consonant = models.ForeignKey(
        Consonant, blank=True, null=True, related_name="consonant_third")
    fourth_consonant = models.ForeignKey(
        Consonant, blank=True, null=True, related_name="consonant_fourth")
    size = models.IntegerField(blank=True, null=True)
    ssp = models.IntegerField(blank=True, null=True)
    cv_structure = models.CharField(blank=True, null=True, max_length=10)
    preferred_consonant = models.CharField(blank=True, null=True, max_length=10)
    nad_vc = models.IntegerField(blank=True, null=True)
    nad_c1c2 = models.FloatField(blank=True, null=True)
    nad_c2c3 = models.FloatField(blank=True, null=True)


class TokenLabel(models.Model):
    label = models.CharField(blank=True, null=True, max_length=15)
    description = models.TextField(blank=True, null=True)
    morphonotacticity = models.ForeignKey(
        SkosConcept, blank=True, null=True, related_name="skos_morphonotacticity")

    def __str__(self):
        return "{}".format(self.label)


class SchwaPresent(models.Model):
    spelling = models.CharField(blank=True, null=True, max_length=15)
    schwaprese = models.ForeignKey(
        SkosConcept, blank=True, null=True, related_name="skos_schwaprese")
    is_no = models.NullBooleanField()
    is_final = models.NullBooleanField()
    is_checked = models.NullBooleanField()
    is_both = models.NullBooleanField()

    def __str__(self):
        return "{}".format(self.spelling)


class OnSet(models.Model):
    rightonset = models.CharField(blank=True, null=True, max_length=15)
    variable = models.ForeignKey(
        SkosConcept, blank=True, null=True, related_name="skos_variable")
    pre_change = models.CharField(blank=True, null=True, max_length=1)
    post_change = models.CharField(blank=True, null=True, max_length=1)
    onset = models.CharField(blank=True, null=True, max_length=15)
    offset = models.CharField(blank=True, null=True, max_length=15)

    def __str__(self):
        return "{}".format(self.rightonset)


class Token(models.Model):
    legacy_id = models.CharField(blank=True, null=True, max_length=15)
    spelling = models.CharField(blank=True, null=True, max_length=15)
    left_context = models.CharField(blank=True, null=True, max_length=150)
    plain_word = models.CharField(blank=True, null=True, max_length=150)
    pos = models.ForeignKey(
        SkosConcept, blank=True, null=True, related_name="skos_pos")
    label = models.ForeignKey(
        TokenLabel, blank=True, null=True, related_name="token_label")
    comments = models.CharField(blank=True, null=True, max_length=150)
    right_context = models.CharField(blank=True, null=True, max_length=150)
    text_source = models.ForeignKey(
        Text, blank=True, null=True, related_name="token_text")
    cluster = models.ForeignKey(
        Cluster, blank=True, null=True, related_name="token_cluster")
    file = models.CharField(blank=True, null=True, max_length=50)
    medial_suffix = models.CharField(blank=True, null=True, max_length=50)
    final_suffix = models.CharField(blank=True, null=True, max_length=50)
    spelling2 = models.ForeignKey(
        SchwaPresent, blank=True, null=True, related_name="token_spelling2")
    rightonset = models.ForeignKey(OnSet, blank=True, null=True, related_name="token_onset")

    def __str__(self):
        return "{}".format(self.plain_word)
