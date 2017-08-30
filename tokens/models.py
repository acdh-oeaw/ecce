from django.db import models
from django.core.urlresolvers import reverse
from vocabs.models import SkosConcept


class Lemma(models.Model):
    """docstring forLemma."""
    name = models.CharField(
        blank=True, null=True, max_length=100, verbose_name="Lemma",
        help_text="Lemma of the word form the cluster is part of"
    )
    pos = models.ForeignKey(
        SkosConcept, blank=True, null=True, related_name="skos_lemma_pos",
        verbose_name="Part of speech (lemma)",
        help_text="Part of speech of word token the cluster is part of"
    )

    def __str__(self):
        return "{} ({})".format(self.name, self.pos.pref_label)

    def get_absolute_url(self):
        return reverse('tokens:lemma_detail', kwargs={'pk': self.id})


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
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}".format(self.dates)

    def get_absolute_url(self):
        return reverse('tokens:date_detail', kwargs={'pk': self.dates})


class Corpus(models.Model):
    name = models.CharField(blank=True, null=True, max_length=100)

    def __str__(self):
        return "{}".format(self.name)

    def get_absolute_url(self):
        return reverse('tokens:corpus_detail', kwargs={'pk': self.id})


class Text(models.Model):
    text = models.CharField(
        blank=True, null=True, max_length=100, verbose_name="Text",
        help_text="Source text the token is extracted from"
    )
    date = models.CharField(
        blank=True, null=True, max_length=100,
        verbose_name="Text", help_text="Date of source  text this token is extracted from"
    )
    genre = models.ForeignKey(
        SkosConcept, blank=True, null=True, related_name="skos_genre",
        verbose_name="Genre", help_text="Genre of source text this token is extracted from"
    )
    corpus = models.ForeignKey(
        Corpus, blank=True, null=True, related_name="text_corpus",
        verbose_name="Corpus", help_text="Corpus of source text this token is extracted from"
    )
    lower = models.IntegerField(
        blank=True, null=True, verbose_name="lower",
        help_text="lower estimate for date"
    )
    mean_date = models.ForeignKey(
        Date, blank=True, null=True, verbose_name="Date",
        help_text="Estimate for date of text this token is extracted from"
    )
    size = models.IntegerField(
        blank=True, null=True, verbose_name="Text Size",
        help_text="Size of source text this token is extracted from"
    )
    dialect = models.ForeignKey(
        SkosConcept, blank=True, null=True, related_name="skos_dialect",
        verbose_name="Region", help_text="Region of source text this token is extracted from"
    )
    updated = models.DateTimeField(
        auto_now=True, verbose_name="updated",
        help_text="Date of last update"
    )

    def __str__(self):
        return "{}".format(self.text)

    def get_absolute_url(self):
        return reverse('tokens:text_detail', kwargs={'pk': self.id})


class Consonant(models.Model):
    consonant = models.CharField(blank=True, null=True, max_length=15)
    art_manner = models.ForeignKey(
        SkosConcept, blank=True, null=True, related_name="skos_art_manner")
    art_place = models.ForeignKey(
        SkosConcept, blank=True, null=True, related_name="skos_art_place")
    voice = models.ForeignKey(
        SkosConcept, blank=True, null=True, related_name="skos_voice")
    airflow = models.ForeignKey(
        SkosConcept, blank=True, null=True, related_name="skos_airflow")
    sonority = models.IntegerField(blank=True, null=True)
    transcription = models.CharField(blank=True, null=True, max_length=15)
    place_ord = models.IntegerField(blank=True, null=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}".format(self.consonant)

    def get_absolute_url(self):
        return reverse('tokens:consonant_detail', kwargs={'pk': self.id})


class Cluster(models.Model):
    consonant = models.CharField(blank=True, null=True, max_length=10)
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
    preferred_cluster = models.CharField(blank=True, null=True, max_length=10)
    nad_vc = models.FloatField(blank=True, null=True)
    nad_c1c2 = models.FloatField(blank=True, null=True)
    nad_c2c3 = models.FloatField(blank=True, null=True)
    updated = models.DateTimeField(auto_now=True)

    @property
    def related_tokens_amount(self):
        tokens = Token.objects.filter(cluster=self.id)
        return len(tokens)

    def __str__(self):
        return "{}".format(self.consonant)

    def get_absolute_url(self):
        return reverse('tokens:cluster_detail', kwargs={'pk': self.id})


class TokenLabel(models.Model):
    label = models.CharField(blank=True, null=True, max_length=15)
    description = models.TextField(blank=True, null=True)
    morphonotacticity = models.ForeignKey(
        SkosConcept, blank=True, null=True, related_name="skos_morphonotacticity"
    )
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}".format(self.label)

    def get_absolute_url(self):
        return reverse('tokens:tokenlabel_detail', kwargs={'pk': self.id})


class SchwaPresent(models.Model):
    spelling = models.CharField(blank=True, null=True, max_length=15)
    schwaprese = models.ForeignKey(
        SkosConcept, blank=True, null=True, related_name="skos_schwaprese")
    is_no = models.NullBooleanField()
    is_final = models.NullBooleanField()
    is_final_v = models.NullBooleanField()
    is_checked = models.NullBooleanField()
    is_both = models.NullBooleanField()
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}".format(self.spelling)

    def get_absolute_url(self):
        return reverse('tokens:schwapresent_detail', kwargs={'pk': self.id})


class OnSet(models.Model):
    rightonset = models.CharField(blank=True, null=True, max_length=15)
    variable = models.ForeignKey(
        SkosConcept, blank=True, null=True, related_name="skos_variable")
    pre_change = models.CharField(blank=True, null=True, max_length=15)
    post_change = models.CharField(blank=True, null=True, max_length=15)
    onset = models.CharField(blank=True, null=True, max_length=15)
    offset = models.CharField(blank=True, null=True, max_length=15)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}".format(self.rightonset)

    def get_absolute_url(self):
        return reverse('tokens:onset_detail', kwargs={'pk': self.id})


class Token(models.Model):
    legacy_id = models.CharField(
        blank=True, null=True, max_length=15, verbose_name="Identifier",
        help_text="Canonical identifier of this token"
    )
    spelling = models.CharField(
        blank=True, null=True, max_length=15, verbose_name="search string",
        help_text="Search string used to find this token"
    )
    left_context = models.CharField(
        blank=True, null=True, max_length=150, verbose_name="Left context",
        help_text="Left context of word token the cluster is part of"
    )
    plain_word = models.CharField(
        blank=True, null=True, max_length=150, verbose_name="Word form",
        help_text="Word token the cluster is part of"
    )
    pos = models.ForeignKey(
        SkosConcept, blank=True, null=True, related_name="skos_pos",
        verbose_name="Part of speech",
        help_text="Part of speech of word token the cluster is part of"
    )
    label = models.ForeignKey(
        TokenLabel, blank=True, null=True, related_name="token_label",
        verbose_name="Morphological status",
        help_text="Morphological status of cluster (e.g. lexical, derivational, inflectional,...)"
    )
    comments = models.CharField(
        blank=True, null=True, max_length=150, verbose_name="internal comments",
        help_text="Comments for internal usage"
    )
    right_context = models.CharField(
        blank=True, null=True, max_length=150, verbose_name="Right context",
        help_text="Right context of word token the cluster is part of"
    )
    text_source = models.ForeignKey(
        Text, blank=True, null=True, related_name="token_text",
        verbose_name="Text",
        help_text="Source text the token is extracted from"
    )
    cluster = models.ForeignKey(
        Cluster, blank=True, null=True, related_name="token_cluster",
        verbose_name="Cluster", help_text="IPA phonological transcription of the cluster"
    )
    file = models.CharField(
        blank=True, null=True, max_length=50, verbose_name="internal analysis file",
        help_text="Internal file name used for data analysis"
    )
    medial_suffix = models.CharField(
        blank=True, null=True, max_length=50, verbose_name="Medial suffix",
        help_text="Medial suffix involved in cluster formation")
    final_suffix = models.CharField(
        blank=True, null=True, max_length=50, verbose_name="Final suffix",
        help_text="Final suffix involved in cluster formation"
    )
    spelling2 = models.ForeignKey(
        SchwaPresent, blank=True, null=True, related_name="token_spelling2",
        verbose_name="Spelling category", help_text="Graphemic category of the cluster"
    )
    rightonset = models.ForeignKey(
        OnSet, blank=True, null=True, related_name="token_onset",
        verbose_name="Right phonological context", help_text="Onset of the following word form"
    )
    updated = models.DateTimeField(
        auto_now=True, verbose_name="Date of last update", help_text="Date of last update"
    )
    lemma = models.ForeignKey(
        Lemma, blank=True, null=True, verbose_name="Word lemma",
        help_text="Lemma of the word form the cluster is part of"
    )
    weight = models.FloatField(
        blank=True, null=True, verbose_name="Weight",
        help_text="Probabilistically derived weight of the cluster token"
    )
    weight_norm = models.FloatField(
        blank=True, null=True, verbose_name="Per semizentury normalized weight",
        help_text="Per million tokens normalized probabilistically derived weigth of the cluster token (normalization based on semicentury-wise subcorpora)")

    def __str__(self):
        return "{}".format(self.plain_word)

    def get_absolute_url(self):
        return reverse('tokens:token_detail', kwargs={'pk': self.id})
