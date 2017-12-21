from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Fieldset, Div, MultiField, HTML
from crispy_forms.bootstrap import *
from tokens.models import *


class GenericFilterFormHelper(FormHelper):

    def __init__(self, *args, **kwargs):
        super(GenericFilterFormHelper, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.form_class = 'genericFilterForm'
        self.form_method = 'GET'
        self.helper.form_tag = False
        self.add_input(Submit('Filter', 'Search'))


class TokenFilterFormHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super(TokenFilterFormHelper, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.form_class = 'genericFilterForm'
        self.form_method = 'GET'
        self.helper.form_tag = False
        self.add_input(Submit('Filter', 'Search'))
        self.layout = Layout(
            Accordion(
                AccordionGroup(
                    'Basic search options',
                    'legacy_id',
                    'left_context',
                    'plain_word',
                    'right_context',
                    'spelling2',
                    css_id="basic_search_fields"
                ),
                AccordionGroup(
                    'Lexicon related search options',
                    'lemma__name',
                    'lemma__pos',
                    css_id="lexicon_search_options"),
                AccordionGroup(
                    'Morphology related search options',
                    'pos',
                    'label',
                    'medial_suffix',
                    'final_suffix',
                    'label__label',
                    'label__description',
                    'label__morphonotacticity',
                    css_id="morphology_search_options"
                ),
                AccordionGroup(
                    'Phonology related search options',
                    'rightonset',
                    'rightonset__variable',
                    'rightonset__pre_change',
                    'rightonset__post_change',
                    'rightonset__onset',
                    'rightonset__offset',
                    #cluster-consonant should be added here

                    css_id="phonology_search_options"),
                AccordionGroup(
                    'Phonotactics related search options',
                    'weight',
                    'weight_norm',
                    'cluster__consonant',
                    'cluster__first_consonant__consonant',
                    'cluster__second_consonant__consonant',
                    'cluster__third_consonant__consonant',
                    'cluster__fourth_consonant__consonant',
                    'cluster__size',
                    'cluster__ssp',
                    'cluster__nad_vc',
                    'cluster__nad_c1c2',
                    'cluster__nad_c2c3',
                    'cluster__preferred_cluster',
                    css_id="phonotactics_search_options"),
                AccordionGroup(
                    'Text related search options',
                    'text_source__genre',
                    'text_source__corpus',
                    'text_source__mean_date',
                    'text_source__size',
                    'text_source__dialect',
                    'text_source',
                    'text_source__mean_date__decade',
                    'text_source__mean_date__semicentury',
                    'text_source__mean_date__century',
                    css_id="text_search_options"),
                css_id="accordion",
                )
            )



class NormTokenFilterFormHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super(NormTokenFilterFormHelper, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.form_class = 'genericFilterForm'
        self.form_method = 'GET'
        self.add_input(Submit('Filter', 'Search'))
        self.layout = Layout(
            Accordion(
                AccordionGroup(
                    'Basic search options',
                    'legacy_id',
                    'spelling',
                    'left_context',
                    'plain_word',
                    'pos',
                    'right_context',
                    'file',
                    'medial_suffix',
                    'final_suffix',
                    'updated',
                    css_id="basic_search_fields"
                ),
                AccordionGroup(
                    'Label search options',
                    'label_label',
                    'label_description',
                    'label_morphonotacticity',
                    css_id="label_search_options"),
                AccordionGroup(
                    'Text search options',
                    'text',
                    'text_date',
                    'text_genre',
                    'text_corpus',
                    'text_lower',
                    'text_size',
                    'text_dialect',
                    'text_mean_date_dates',
                    'text_mean_date_decade',
                    'text_mean_date_semicentury',
                    'text_mean_date_century',
                    'text_mean_date_pr_cc_checked',
                    'text_mean_date_pr_cc_final',
                    'text_mean_date_pr_cc_final_V',
                    'text_mean_date_pr_cc_both',
                    'text_mean_date_pr_cc_no',
                    css_id="text_search_options"
                ),
                AccordionGroup(
                    'Cluster search options',
                    # 'cluster_consonant',
                    Div(
                        'cluster_first_consonant',
                        'cluster_first_consonant_art_manner',
                        'cluster_first_consonant_art_place',
                        'cluster_first_consonant_voice',
                        'cluster_first_consonant_airflow',
                        'cluster_first_consonant_sonority',
                        'cluster_first_consonant_transcription',
                        'cluster_first_consonant_place_ord',
                        css_class="consonants",),
                    Div(
                        'cluster_second_consonant',
                        'cluster_second_consonant_art_manner',
                        'cluster_second_consonant_art_place',
                        'cluster_second_consonant_voice',
                        'cluster_second_consonant_airflow',
                        'cluster_second_consonant_sonority',
                        'cluster_second_consonant_transcription',
                        'cluster_second_consonant_place_ord',
                        css_class="consonants"),
                    Div(
                        'cluster_third_consonant',
                        'cluster_third_consonant_art_manner',
                        'cluster_third_consonant_art_place',
                        'cluster_third_consonant_voice',
                        'cluster_third_consonant_airflow',
                        'cluster_third_consonant_sonority',
                        'cluster_third_consonant_transcription',
                        'cluster_third_consonant_place_ord',
                        css_class="consonants"),
                    Div(
                        'cluster_fourth_consonant',
                        'cluster_fourth_consonant_art_manner',
                        'cluster_fourth_consonant_art_place',
                        'cluster_fourth_consonant_voice',
                        'cluster_fourth_consonant_airflow',
                        'cluster_fourth_consonant_sonority',
                        'cluster_fourth_consonant_transcription',
                        'cluster_fourth_consonant_place_ord',
                        css_class="consonants"),

                    'cluster_size',
                    'cluster_ssp',
                    'cluster_cv_structure',
                    'cluster_preferred_cluster',
                    'cluster_nad_vc',
                    'cluster_nad_c1c2',
                    'cluster_nad_c2c3',
                    css_id="cluster_search_options"
                ),
                AccordionGroup(
                    'Spelling search options',
                    'spelling_spelling',
                    'spelling_schwaprese',
                    'spelling_is_no',
                    'spelling_is_final',
                    'spelling_is_final_v',
                    'spelling_is_checked',
                    'spelling_is_both',
                    css_id="spelling_search_options"),
                AccordionGroup(
                    'Rightonset search options',
                    'rightonset',
                    'rightonset_variable',
                    'rightonset_pre_change',
                    'rightonset_post_change',
                    'rightonset_onset',
                    'rightonset_offset',
                    css_id="rightonset_search_options"),
                css_id="accordion",
                )
            )


class TokenCustomFilterFormHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super(TokenCustomFilterFormHelper, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.form_class = 'genericFilterForm'
        self.form_method = 'GET'
        self.helper.form_tag = False
        self.add_input(Submit('Filter', 'Search'))
        self.layout = Layout(
                Fieldset(
                    'Custom search options',
                    'cluster__first_consonant__consonant',
                    'cluster__second_consonant__consonant',
                    'cluster__third_consonant__consonant',
                    'cluster__fourth_consonant__consonant',
                    'cluster__first_consonant__art_manner',
                    'cluster__second_consonant__art_manner',
                    'cluster__third_consonant__art_manner',
                    'cluster__fourth_consonant__art_manner',
                    'cluster__first_consonant__art_place',
                    'cluster__second_consonant__art_place',
                    'cluster__third_consonant__art_place',
                    'cluster__fourth_consonant__art_place',
                    'cluster__first_consonant__voice',
                    'cluster__second_consonant__voice',
                    'cluster__third_consonant__voice',
                    'cluster__fourth_consonant__voice',
                    'text_source__mean_date__dates',
                    css_id="phonotactics_search_options")
                )