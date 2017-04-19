from edc_constants.constants import OTHER, YES

from ..constants import POSITIVE
from ..models import Microbiology
from .form_mixins import SubjectModelFormMixin


class MicrobiologyForm(SubjectModelFormMixin):

    def clean(self):

        self.required_if(
            YES,
            field='urine_culture_performed',
            field_required='urine_culture_results')

        self.required_if(
            POSITIVE,
            field='urine_culture_results',
            field_required='urine_culture_organism')

        self.required_if(
            OTHER,
            field='urine_culture_organism',
            field_required='urine_culture_organism_other')

        self.required_if(
            YES,
            field='blood_culture_performed',
            field_required='blood_culture_results')

        self.required_if(
            POSITIVE,
            field='blood_culture_results',
            field_required='study_day_positive_blood_taken')

        self.required_if(
            POSITIVE,
            field='blood_culture_results',
            field_required='blood_culture_organism')

        self.required_if(
            OTHER,
            field='blood_culture_organism',
            field_required='blood_culture_organism_other')

        self.required_if(
            POSITIVE,
            field='sputum_results_culture',
            field_required='sputum_results_if_positive')

        self.required_if(
            YES,
            field='tissue_biopsy_taken',
            field_required='tissue_biopsy_results')

        self.required_if(
            YES,
            field='tissue_biopsy_results',
            field_required='study_day_positive_biopsy_taken')

        self.required_if(
            YES,
            field='tissue_biopsy_results',
            field_required='tissue_biopsy_organism')

        self.required_if(
            YES,
            field='tissue_biopsy_results',
            field_required='tissue_biopsy_organism_other')

    class Meta:
        model = Microbiology
        fields = '__all__'