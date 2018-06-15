from ambition_validators import LumbarPunctureCsfFormValidator

from ..models import LumbarPunctureCsf
from .form_mixins import SubjectModelFormMixin


class LumbarPunctureCsfForm(SubjectModelFormMixin):

    form_validator_cls = LumbarPunctureCsfFormValidator

    def clean(self):
        cleaned_data = self.cleaned_data
        if cleaned_data.get('qc_requisition'):
            if not cleaned_data.get("quantitative_culture") and not cleaned_data.get("quantitative_culture") == 0:
                msg = 'Quantitative culture is required.'
                self._errors["quantitative_culture"] = self.error_class([msg])
        return cleaned_data

    class Meta:
        model = LumbarPunctureCsf
        fields = '__all__'
