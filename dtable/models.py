from django.db import models
from django.core.urlresolvers import reverse
from django.utils import timezone


class NormToken(models.Model):
    legacy_id = models.CharField(blank=True, null=True, max_length=15)
    spelling = models.CharField(blank=True, null=True, max_length=15)
    left_context = models.CharField(blank=True, null=True, max_length=150)
    plain_word = models.CharField(blank=True, null=True, max_length=150)
    right_context = models.CharField(blank=True, null=True, max_length=150)
    pos = models.CharField(blank=True, null=True, max_length=150)
    label_label = models.CharField(blank=True, null=True, max_length=150)
    label_description = models.TextField(blank=True, null=True)
    label_morphonotacticity = models.CharField(blank=True, null=True, max_length=150)
    comments = models.TextField(blank=True, null=True)
    text = models.CharField(blank=True, null=True, max_length=150)
    text_date = models.CharField(blank=True, null=True, max_length=150)
    text_genre = models.CharField(blank=True, null=True, max_length=150)
    text_corpus = models.CharField(blank=True, null=True, max_length=150)
    text_lower = models.IntegerField(blank=True, null=True)
    text_size = models.IntegerField(blank=True, null=True)
    text_dialect = models.CharField(blank=True, null=True, max_length=150)
    text_mean_date_dates = models.IntegerField(blank=True, null=True)
    text_mean_date_decade = models.IntegerField(blank=True, null=True)
    text_mean_date_semicentury = models.IntegerField(blank=True, null=True)
    text_mean_date_century = models.IntegerField(blank=True, null=True)
    text_mean_date_pr_cc_checked = models.FloatField(blank=True, null=True)
    text_mean_date_pr_cc_final = models.FloatField(blank=True, null=True)
    text_mean_date_pr_cc_final_V = models.FloatField(blank=True, null=True)
    text_mean_date_pr_cc_both = models.FloatField(blank=True, null=True)
    text_mean_date_pr_cc_no = models.IntegerField(blank=True, null=True)
    cluster_consonant = models.CharField(blank=True, null=True, max_length=150)
    cluster_first_consonant = models.CharField(blank=True, null=True, max_length=150)
    cluster_first_consonant_art_manner = models.CharField(blank=True, null=True, max_length=150)
    cluster_first_consonant_art_place = models.CharField(blank=True, null=True, max_length=150)
    cluster_first_consonant_voice = models.CharField(blank=True, null=True, max_length=150)
    cluster_first_consonant_airflow = models.CharField(blank=True, null=True, max_length=150)
    cluster_first_consonant_sonority = models.IntegerField(blank=True, null=True)
    cluster_first_consonant_transcription = models.CharField(blank=True, null=True, max_length=15)
    cluster_first_consonant_place_ord = models.IntegerField(blank=True, null=True)
    cluster_second_consonant = models.CharField(blank=True, null=True, max_length=150)
    cluster_second_consonant_art_manner = models.CharField(blank=True, null=True, max_length=150)
    cluster_second_consonant_art_place = models.CharField(blank=True, null=True, max_length=150)
    cluster_second_consonant_voice = models.CharField(blank=True, null=True, max_length=150)
    cluster_second_consonant_airflow = models.CharField(blank=True, null=True, max_length=150)
    cluster_second_consonant_sonority = models.IntegerField(blank=True, null=True)
    cluster_second_consonant_transcription = models.CharField(blank=True, null=True, max_length=15)
    cluster_second_consonant_place_ord = models.IntegerField(blank=True, null=True)
    cluster_third_consonant = models.CharField(blank=True, null=True, max_length=150)
    cluster_third_consonant_art_manner = models.CharField(blank=True, null=True, max_length=150)
    cluster_third_consonant_art_place = models.CharField(blank=True, null=True, max_length=150)
    cluster_third_consonant_voice = models.CharField(blank=True, null=True, max_length=150)
    cluster_third_consonant_airflow = models.CharField(blank=True, null=True, max_length=150)
    cluster_third_consonant_sonority = models.IntegerField(blank=True, null=True)
    cluster_third_consonant_transcription = models.CharField(blank=True, null=True, max_length=15)
    cluster_third_consonant_place_ord = models.IntegerField(blank=True, null=True)
    cluster_fourth_consonant = models.CharField(blank=True, null=True, max_length=150)
    cluster_fourth_consonant_art_manner = models.CharField(blank=True, null=True, max_length=150)
    cluster_fourth_consonant_art_place = models.CharField(blank=True, null=True, max_length=150)
    cluster_fourth_consonant_voice = models.CharField(blank=True, null=True, max_length=150)
    cluster_fourth_consonant_airflow = models.CharField(blank=True, null=True, max_length=150)
    cluster_fourth_consonant_sonority = models.IntegerField(blank=True, null=True)
    cluster_fourth_consonant_transcription = models.CharField(blank=True, null=True, max_length=15)
    cluster_fourth_consonant_place_ord = models.IntegerField(blank=True, null=True)
    cluster_size = models.IntegerField(blank=True, null=True)
    cluster_ssp = models.IntegerField(blank=True, null=True)
    cluster_cv_structure = models.CharField(blank=True, null=True, max_length=10)
    cluster_preferred_cluster = models.CharField(blank=True, null=True, max_length=10)
    cluster_nad_vc = models.FloatField(blank=True, null=True)
    cluster_nad_c1c2 = models.FloatField(blank=True, null=True)
    cluster_nad_c2c3 = models.FloatField(blank=True, null=True)
    file = models.CharField(blank=True, null=True, max_length=150)
    medial_suffix = models.CharField(blank=True, null=True, max_length=150)
    final_suffix = models.CharField(blank=True, null=True, max_length=150)
    spelling_spelling = models.CharField(blank=True, null=True, max_length=150)
    spelling_schwaprese = models.CharField(blank=True, null=True, max_length=150)
    spelling_is_no = models.NullBooleanField()
    spelling_is_final = models.NullBooleanField()
    spelling_is_final_v = models.NullBooleanField()
    spelling_is_checked = models.NullBooleanField()
    spelling_is_both = models.NullBooleanField()
    rightonset = models.CharField(blank=True, null=True, max_length=150)
    rightonset_variable = models.CharField(blank=True, null=True, max_length=150)
    rightonset_pre_change = models.CharField(blank=True, null=True, max_length=150)
    rightonset_post_change = models.CharField(blank=True, null=True, max_length=150)
    rightonset_onset = models.CharField(blank=True, null=True, max_length=150)
    rightonset_offset = models.CharField(blank=True, null=True, max_length=150)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}".format(self.plain_word)

    def get_absolute_url(self):
        return reverse('tokens:token_detail', kwargs={'pk': self.id})
