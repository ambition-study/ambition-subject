from django.contrib import admin

from edc_base.modeladmin_mixins import audit_fieldset_tuple

from ..admin_site import ambition_subject_admin
from ..forms import DeathReportForm
from ..models import DeathReport
from .modeladmin_mixins import CrfModelAdminMixin


@admin.register(DeathReport, site=ambition_subject_admin)
class DeathReportAdmin(CrfModelAdminMixin, admin.ModelAdmin):

    form = DeathReportForm

    radio_fields = {
        'death_as_inpatient': admin.VERTICAL,
        'cause_of_death_study_doctor_opinion': admin.VERTICAL,
        'cause_tb_study_doctor_opinion': admin.VERTICAL}

    fieldsets = (
        (None, {
            'fields': (
                'subject_visit',
                'death_datetime',
                'study_day',
                'death_as_inpatient')},
         ),
        ('Opinion of Local Study Doctor', {
            'fields': (
                'cause_of_death_study_doctor_opinion',
                'cause_other_study_doctor_opinion',
                'cause_tb_study_doctor_opinion')}),
        ('Summary', {
            'fields': (
                'death_narrative',)}),
        audit_fieldset_tuple
    )
