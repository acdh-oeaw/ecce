from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Fieldset, Div, MultiField
from tokens.models import *


class GenericFilterFormHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super(GenericFilterFormHelper, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.form_class = 'genericFilterForm'
        self.form_method = 'GET'
        self.add_input(Submit('Filter', 'Search'))


class NormTokenFilterFormHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super(NormTokenFilterFormHelper, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.form_class = 'genericFilterForm'
        self.form_method = 'GET'
        self.add_input(Submit('Filter', 'Search'))
        self.layout = Layout(
            Fieldset(
                'Basic search options',
                Div('legacy_id',
                'spelling',
                'left_context',
                'plain_word',
                'pos',
                'right_context',
                'file',
                'medial_suffix',
                'final_suffix',
                'updated',
                css_class="panel"),
                css_id="basic_search_fields",
                css_class="button"),
            Fieldset(
                'Label search options',
                'label_label',
                'label_description',
                'label_morphonotacticity',
                css_id="label_search_options"),
            Fieldset(
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
                css_id="text_search_options"),
             Fieldset(
                'Cluster search options',
                'cluster_consonant',
                Div(
                	'cluster_first_consonant_consonant',
	                'cluster_first_consonant_art_manner',
	                'cluster_first_consonant_art_place',
	                'cluster_first_consonant_voice',
	                'cluster_first_consonant_airflow',
	                'cluster_first_consonant_sonority',
	                'cluster_first_consonant_transcription',
	                'cluster_first_consonant_place_ord',
                	css_class="consonants",),
                Div(
                	'cluster_second_consonant_consonant',
	                'cluster_second_consonant_art_manner',
	                'cluster_second_consonant_art_place',
	                'cluster_second_consonant_voice',
	                'cluster_second_consonant_airflow',
	                'cluster_second_consonant_sonority',
	                'cluster_second_consonant_transcription',
	                'cluster_second_consonant_place_ord',
                	css_class="consonants"),
                Div(
                	'cluster_third_consonant_consonant',
	                'cluster_third_consonant_art_manner',
	                'cluster_third_consonant_art_place',
	                'cluster_third_consonant_voice',
	                'cluster_third_consonant_airflow',
	                'cluster_third_consonant_sonority',
	                'cluster_third_consonant_transcription',
	                'cluster_third_consonant_place_ord',
                	css_class="consonants"),
                Div(
                	'cluster_fourth_consonant_consonant',
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
                css_id="cluster_search_options"),
             Fieldset(
                'Spelling search options',
                'spelling_spelling',
                'spelling_schwaprese',
                'spelling_is_no',
                'spelling_is_final',
                'spelling_is_final_v',
                'spelling_is_checked',
                'spelling_is_both',
                css_id="spelling_search_options"),
            Fieldset(
                'Rightonset search options',
                'rightonset',
                'rightonset_variable',
                'rightonset_pre_change',
                'rightonset_post_change',
                'rightonset_onset',
                'rightonset_offset',
                css_id="rightonset_search_options"),   
                
            )