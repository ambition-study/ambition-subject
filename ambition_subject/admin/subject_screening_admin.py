from django.contrib import admin

from ..models import SubjectScreening
from ..admin_site import ambition_subject_admin


@admin.register(SubjectScreening, site=ambition_subject_admin)
class SubjectScreeningAdmin(ModelAdminMixin, admin.ModelAdmin):

    form = SubjectScreeningForm

    radio_fields = {
        'gender': admin.VERTICAL,
        'meningitis_dx': admin.VERTICAL,
        'will_hiv_test': admin.VERTICAL,
        'mental_status': admin.VERTICAL,
        'consent_ability': admin.VERTICAL,
        'pregnancy_or_lactation': admin.VERTICAL,
        'previous_drug_reaction': admin.VERTICAL,
        'contraindicated_meds': admin.VERTICAL,
        'received_amphotericin': admin.VERTICAL,
        'received_fluconazole': admin.VERTICAL, }

    fieldsets = (
        (None, {
            'fields': (
                'report_datetime',
                'gender',
                'age_in_years',
                'meningitis_dx',
                'will_hiv_test',
                'mental_status',
                'consent_ability',
                'pregnancy_or_lactation',
                'preg_test_date',
                'previous_drug_reaction',
                'contraindicated_meds',
                'received_amphotericin',
                'received_fluconazole')
        }),
    )

    def get_readonly_fields(self, request, obj=None):
        return (super().get_readonly_fields(request, obj=obj))
