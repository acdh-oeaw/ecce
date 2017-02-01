from dtable.models import *
from tokens.models import *

tokens = Token.objects.exclude(cluster__isnull=True)
errors = []
for x in tokens[:5]:
    temp_new,_ = NormToken.objects.get_or_create(legacy_id=x.legacy_id)
    temp_new.spelling = x.spelling
    temp_new.left_context = x.left_context
    temp_new.plain_word = x.plain_word
    temp_new.right_context = x.right_context
    try:
        temp_new.pos = x.pos.pref_label
        temp_new.label_label = x.label.label
        temp_new.label_description = x.label.description
        temp_new.label_morphonotacticity = x.label.morphonotacticity.pref_label
    except:
        errors.append(['missing label :',x])
    temp_new.comments = x.comments
    try:
        temp_new.text = x.text_source.text
        temp_new.text_date = x.text_source.date
        temp_new.text_genre = x.text_source.genre.pref_label
        temp_new.text_corpus = x.text_source.corpus.name
        temp_new.text_lower = x.text_source.lower
        temp_new.text_size = x.text_source.size
        temp_new.text_dialect = x.text_source.dialect.pref_label
        temp_new.text_mean_date_dates = x.text_source.mean_date.dates
        temp_new.text_mean_date_decade = x.text_source.mean_date.decade
        temp_new.text_mean_date_semicentury = x.text_source.mean_date.semicentury
        temp_new.text_mean_date_century = x.text_source.mean_date.century
        temp_new.text_mean_date_pr_cc_checked = x.text_source.mean_date.pr_cc_checekd
    except:
        errors.append(['missing text :',x])
    temp_new.cluster_consonant = x.cluster.consonant
    try:
        temp_new.cluster_first_consonant = x.cluster.first_consonant.consonant
        temp_new.cluster_first_consonant_art_manner = x.cluster.first_consonant.art_manner.pref_label
        temp_new.cluster_first_consonant_art_place = x.cluster.first_consonant.art_place.pref_label
        temp_new.cluster_first_consonant_voice = x.cluster.first_consonant.voice.pref_label
        temp_new.cluster_first_consonant_airflow = x.cluster.first_consonant.airflow.pref_label
        temp_new.cluster_first_consonant_sonority = x.cluster.first_consonant.sonority
        temp_new.cluster_first_consonant_transcription = x.cluster.first_consonant.transcription
        temp_new.cluster_first_consonant_place_ord = x.cluster.first_consonant.place_ord
    except:
        errors.append(["missing first consonant :",x])
    try:
        temp_new.cluster_second_consonant = x.cluster.second_consonant.consonant
        temp_new.cluster_second_consonant_art_manner = x.cluster.second_consonant.art_manner.pref_label
        temp_new.cluster_second_consonant_art_place = x.cluster.second_consonant.art_place.pref_label
        temp_new.cluster_second_consonant_voice = x.cluster.second_consonant.voice.pref_label
        temp_new.cluster_second_consonant_airflow = x.cluster.second_consonant.airflow.pref_label
        temp_new.cluster_second_consonant_sonority = x.cluster.second_consonant.sonority
        temp_new.cluster_second_consonant_transcription = x.cluster.second_consonant.transcription
        temp_new.cluster_second_consonant_place_ord = x.cluster.second_consonant.place_ord
    except:
        errors.append(["missing second consonant :",x])
    try:
        temp_new.cluster_third_consonant = x.cluster.third_consonant.consonant
        temp_new.cluster_third_consonant_art_manner = x.cluster.third_consonant.art_manner.pref_label
        temp_new.cluster_third_consonant_art_place = x.cluster.third_consonant.art_place.pref_label
        temp_new.cluster_third_consonant_voice = x.cluster.third_consonant.voice.pref_label
        temp_new.cluster_third_consonant_airflow = x.cluster.third_consonant.airflow.pref_label
        temp_new.cluster_third_consonant_sonority = x.cluster.third_consonant.sonority
        temp_new.cluster_third_consonant_transcription = x.cluster.third_consonant.transcription
        temp_new.cluster_third_consonant_place_ord = x.cluster.third_consonant.place_ord
    except:
        errors.append(["missing first consonant :",x])
    try:
        temp_new.cluster_fourth_consonant = x.cluster.fourth_consonant.consonant
        temp_new.cluster_fourth_consonant_art_manner = x.cluster.fourth_consonant.art_manner.pref_label
        temp_new.cluster_fourth_consonant_art_place = x.cluster.fourth_consonant.art_place.pref_label
        temp_new.cluster_fourth_consonant_voice = x.cluster.fourth_consonant.voice.pref_label
        temp_new.cluster_fourth_consonant_airflow = x.cluster.fourth_consonant.airflow.pref_label
        temp_new.cluster_fourth_consonant_sonority = x.cluster.fourth_consonant.sonority
        temp_new.cluster_fourth_consonant_transcription = x.cluster.fourth_consonant.transcription
        temp_new.cluster_fourth_consonant_place_ord = x.cluster.fourth_consonant.place_ord
    except:
        errors.append(["missing fourth consonant :",x])
    temp_new.cluster_size = x.cluster.size
    temp_new.cluster_ssp = x.cluster.ssp
    temp_new.cluster_cv_structure = x.cluster.cv_structure
    temp_new.cluster_preferred_cluster = x.cluster.preferred_cluster
    temp_new.cluster_nad_vc = x.cluster.nad_vc
    temp_new.cluster_nad_c1c2 = x.cluster.nad_c1c2
    temp_new.cluster_nad_c2c3 = x.cluster.nad_c2c3
    temp_new.file = x.file
    temp_new.medial_suffix = x.medial_suffix
    temp_new.final_suffix = x.final_suffix
    try:
        temp_new.spelling = x.spelling2.spelling
        temp_new.spelling_schwaprese = x.spelling2.schwaprese.pref_label
        temp_new.spelling_is_no = x.spelling2.is_no
        temp_new.is_final = x.spelling2.is_final
        temp_new.spelling_is_final_v = x.spelling2.is_final_v
        temp_new.spelling_is_checked = x.spelling2.is_checked
        temp_new.spelling_is_both = x.spelling2.is_both
    except:
        errors.append(['missing spelling :',x])
    try:
        temp_new.rightonset = x.rightonset.rightonset
        temp_new.rightonset_variable = x.rightonset.variable.pref_label
        temp_new.rightonset_pre_change = x.rightonset.pre_change
        temp_new.rightonset_post_change = x.rightonset.post_change
        temp_new.rightonset_onset = x.rightonset.onset
        temp_new.rightonset_offset = x.rightonset.offset
    except:
        errors.append(["no right on set:",x])
    temp_new.save()
print(len(NormToken.objects.all()))
