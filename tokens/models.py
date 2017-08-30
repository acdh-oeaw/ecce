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
    dates = models.IntegerField(
        primary_key=True, verbose_name="Date",
        help_text="Date of source text this token is extracted from"
    )
    decade = models.IntegerField(
        blank=True, null=True, verbose_name="Decade",
        help_text="Decade of source text this token is extracted from"
    )
    semicentury = models.IntegerField(
        blank=True, null=True, verbose_name="Semicentury",
        help_text="50-year period of source text this token is extracted from (e.g. 1250 stands for 1250-1300)"
    )
    century = models.IntegerField(
        blank=True, null=True, verbose_name="Century",
        help_text="Century of source text this token is extracted from"
    )
    pr_cc_checekd = models.FloatField(
        blank=True, null=True, verbose_name="pr_cc_checked",
        help_text="probability estimate of graphemically checked cluster for this year (for probabilistic estimation only)"
    )
    pr_cc_final = models.FloatField(
        blank=True, null=True, verbose_name="pr_cc_final",
        help_text="probability estimate of cluster with graphemic final schwa for this year (for probabilistic estimation only)"
    )
    pr_cc_final_V = models.FloatField(
        blank=True, null=True, verbose_name="pr_cc_final_V",
        help_text="probability estimate of cluster with graphemic final and checked schwa for this year (for probabilistic estimation only)")
    pr_cc_both = models.FloatField(
        blank=True, null=True, verbose_name="pr_cc_both",
        help_text="probability estimate of cluster with graphemic final schwa before vowel for this year (for probabilistic estimation only)"
    )
    pr_cc_no = models.IntegerField(
        blank=True, null=True, verbose_name="pr_cc_no",
        help_text="probability estimate of graphemic cluster for this year (for probabilistic estimation only)"
    )
    updated = models.DateTimeField(
        auto_now=True, verbose_name="updated", help_text="Date of last update"
    )

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
    consonant = models.CharField(
        blank=True, null=True, max_length=10,
        verbose_name="Cluster", help_text="IPA phonological transcription of the cluster"
    )
    first_consonant = models.ForeignKey(
        Consonant, blank=True, null=True, related_name="consonant_first",
        verbose_name="Fourth-to-last segment",
        help_text="IPA phonological transcription of fourth-to-last segment of the cluster (only applies to CCCC)"
    )
    second_consonant = models.ForeignKey(
        Consonant, blank=True, null=True, related_name="consonant_second",
        verbose_name="Third-to-last segment",
        help_text="IPA phonological transcription of third-to-last segment of the cluster (only applies to CCC(C))"
    )
    third_consonant = models.ForeignKey(
        Consonant, blank=True, null=True, related_name="consonant_third",
        verbose_name="Second-to-last segment",
        help_text="IPA phonological transcription of penultimate segment of the cluster"
    )
    fourth_consonant = models.ForeignKey(
        Consonant, blank=True, null=True, related_name="consonant_fourth",
        verbose_name="Last segment",
        help_text="IPA phonological transcription of fourth-to-last segment of the cluster (only applies to CCCC)"
    )
    size = models.IntegerField(
        blank=True, null=True, verbose_name="Cluster size",
        help_text="Number of segments in the cluster"
    )
    ssp = models.IntegerField(
        blank=True, null=True, verbose_name="SSP fulfilled",
        verbose_name="Says if sonority sequencing principle is fulfilled for this cluster"
    )
    cv_structure = models.CharField(
        blank=True, null=True, max_length=10, verbose_name="cv_structure",
        help_text="Segmental structure of this cluster"
    )
    preferred_cluster = models.CharField(
        blank=True, null=True, max_length=10,
        verbose_name="NAD preferred",
        help_text="Says if cluster is preferred according to net auditory distance (see http://wa.amu.edu.pl/nadcalc/)"
    )
    nad_vc = models.FloatField(
        blank=True, null=True, verbose_name="NAD VC",
        help_text="Net auditory distance between preceding vowel and penultimate segment (see http://wa.amu.edu.pl/nadcalc/)"
    )
    nad_c1c2 = models.FloatField(
        blank=True, null=True, verbose_name="NAD C1C2", help_text="Net auditory distance between segment 1 and segment 2 (see http://wa.amu.edu.pl/nadcalc/)"
    )
    nad_c2c3 = models.FloatField(
        blank=True, null=True, verbose_name="NAD C2C3",
        help_text="Net auditory distance between segment 1 and segment 2 (see http://wa.amu.edu.pl/nadcalc/)")
    updated = models.DateTimeField(
        auto_now=True, verbose_name="updated", help_text="Date of last update"
    )

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
    spelling = models.CharField(
        blank=True, null=True, max_length=15, verbose_name="Spelling category",
        help_text="Graphemic category of the cluster"
    )
    schwaprese = models.ForeignKey(
        SkosConcept, blank=True, null=True, related_name="skos_schwaprese",
        verbose_name="schwa present category",
        help_text="classification of spelling category (for probabilistic estimation only)"
    )
    is_no = models.NullBooleanField(
        verbose_name="schwa not present",
        help_text="says if schwa is graphemically represented (for probabilistic estimation only)"
    )
    is_final = models.NullBooleanField(
        verbose_name="schwa finally present",
        help_text="says if schwa is graphemically represented in word final position (for probabilistic estimation only)"
    )
    is_final_v = models.NullBooleanField(
        verbose_name="schwa finally_V present",
        help_text="says if schwa is graphemically represented in word final position before vowel (for probabilistic estimation only)"
    )
    is_checked = models.NullBooleanField(
        verbose_name="checked schwa present",
        help_text="says if schwa is graphemically represented in interconsonantal position (for probabilistic estimation only)"
    )
    is_both = models.NullBooleanField(
        verbose_name="both schwas present",
        help_text="says if schwa is graphemically represented in both positions"
    )
    updated = models.DateTimeField(
        auto_now=True, verbose_name="updated", help_text="Date of last update"
    )

    def __str__(self):
        return "{}".format(self.spelling)

    def get_absolute_url(self):
        return reverse('tokens:schwapresent_detail', kwargs={'pk': self.id})


class OnSet(models.Model):
    rightonset = models.CharField(
        blank=True, null=True, max_length=15, verbose_name="Right phonological context",
        help_text="Phonological onset of the following word form"
    )
    variable = models.ForeignKey(
        SkosConcept, blank=True, null=True, related_name="skos_variable",
        verbose_name="Variability of right context",
        help_text="Stability status of the onset of the following wordform (fixed or variable)"
    )
    pre_change = models.CharField(
        blank=True, null=True, max_length=15, verbose_name="Status pre change of context",
        help_text="Phonological value before a potential sound change of the following onset"
    )
    post_change = models.CharField(
        blank=True, null=True, max_length=15, verbose_name="Status post change of context",
        help_text="Phonological value after a potential sound change of the following onset"
    )
    onset = models.CharField(
        blank=True, null=True, max_length=15, verbose_name="Onset of change",
        help_text="Onset of sound change of the following phonological onset"
    )
    offset = models.CharField(
        blank=True, null=True, max_length=15, verbose_name="Offset of change",
        help_text="Offset of sound change of the following phonological onset"
    )
    updated = models.DateTimeField(
        auto_now=True, verbose_name="updated", help_text="Date of last update"
    )

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
