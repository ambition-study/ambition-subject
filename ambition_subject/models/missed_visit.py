from django.db import models

from edc_base.model_managers import HistoricalRecords
from edc_base.model_mixins import BaseUuidModel
from edc_base.model_validators import date_not_future

from .list_models import MissedVisitReason


class MissedVisit(BaseUuidModel):

    missed_study_visit_date = models.DateField(
        validators=[date_not_future])

    visit_missed = models.DecimalField(
        decimal_places=1,
        help_text='Insert visit code',
        max_digits=3)

    missed_visit_reason = models.ManyToManyField(
        MissedVisitReason,
        verbose_name='Reason(s) why participant missed the study visit;')

    missed_visit_reason_other = models.CharField(
        blank=True,
        max_length=50,
        null=True,
        verbose_name='If other reason, please specify:')

    notes_or_action_taken = models.TextField()

    history = HistoricalRecords()

    class Meta:
        app_label = 'ambition_subject'