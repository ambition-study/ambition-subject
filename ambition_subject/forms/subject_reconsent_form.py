from django import forms
from django.core.exceptions import ObjectDoesNotExist
from edc_form_validators import FormValidatorMixin
from edc_registration.models import RegisteredSubject

from ..models import SubjectReconsent


class SubjectReconsentForm(FormValidatorMixin, forms.ModelForm):

    subject_identifier = forms.CharField(
        label='Subject identifier',
        widget=forms.TextInput(attrs={'readonly': 'readonly'}))

    def clean(self):
        cleaned_data = super().clean()
        try:
            RegisteredSubject.objects.get(
                subject_identifier=cleaned_data.get('subject_identifier'),
                identity=cleaned_data.get('identity'))
        except ObjectDoesNotExist:
            raise forms.ValidationError({
                'identity': 'Identity number does not match.'})
        return cleaned_data

    class Meta:
        model = SubjectReconsent
        fields = '__all__'