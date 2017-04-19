from edc_constants.constants import YES, NO

from ..constants import NVP
from ..models import PatientHistory
from .form_mixins import SubjectModelFormMixin


class PatientHistoryForm(SubjectModelFormMixin):

    def clean(self):
        cleaned_data = super().clean()

        condition = cleaned_data.get('arvs') and NVP in cleaned_data.get('arvs')

        self.required_if(YES, field='med_history', field_required='tb_site')
        self.required_if(
            YES, field='tb_treatment', field_required='taking_rifampicin')
        self.required_if(
            YES, field='taking_rifampicin', field_required='rifampicin_started_date')
        self.required_if(
            YES, field='previous_infection', field_required='infection_date')
        self.required_if(YES, field='taking_arv', field_required='arv_date')
        self.required_if(YES, field='taking_arv', field_required='arvs')
        self.required_if_true(condition, field_required='first_line_choice')
        self.required_if(
            NO, field='patient_adherence', field_required='last_dose')
        self.required_if(
            YES, field='other_medications', field_required='specify_medications')

    class Meta:
        model = PatientHistory
        fields = '__all__'