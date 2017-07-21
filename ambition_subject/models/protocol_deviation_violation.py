from django.db import models

from edc_base.model_managers import HistoricalRecords
from edc_base.model_validators import date_not_future
from edc_constants.choices import YES_NO

from ..choices import PROTOCOL_VIOLATION, ACTION_REQUIRED, DEVIATION_VIOLATION

from .model_mixins import CrfModelMixin


class ProtocolDeviationViolation(CrfModelMixin):

    deviation_or_violation = models.CharField(
        verbose_name='Is this a protocol deviation or violation?',
        max_length=5,
        choices=DEVIATION_VIOLATION
    )

    participant_safety_impact = models.CharField(
        verbose_name='Could this occurrence have an impact on safety of the '
                     'participant?',
        max_length=5,
        choices=YES_NO)

    participant_safety_impact_details = models.TextField(
        verbose_name='If yes, details:',
        null=True,
        blank=True)

    study_outcomes_impact = models.CharField(
        verbose_name='Could this occurrence have an impact on Study outcomes?',
        max_length=5,
        choices=YES_NO)

    study_outcomes_impact_details = models.TextField(
        verbose_name='If yes, details:',
        null=True,
        blank=True)

    date_violation_datetime = models.DateTimeField(
        verbose_name='Date violation occured:',
        validators=[date_not_future],
        null=True,
        blank=True)

    protocol_violation_type = models.CharField(
        verbose_name='Type of Protocol Violation/Deviation:',
        max_length=70,
        choices=PROTOCOL_VIOLATION,
        null=True,
        blank=True)

    other_protocol_violation_type = models.CharField(
        null=True,
        blank=True,
        verbose_name='If other, please specify:',
        max_length=50)

    violation_description = models.TextField(
        verbose_name='Describe the violation fully. How the violation '
                     'happened, what occurred?',
        null=True,
        blank=True)

    violation_reason = models.TextField(
        verbose_name='Explain the reason why the violation occurred:',
        null=True,
        blank=True)

    corrective_action_datetime = models.DateTimeField(
        verbose_name='Corrective action date and time:',
        validators=[date_not_future],
        null=True,
        blank=True)

    corrective_action = models.CharField(
        verbose_name='Corrective action taken:',
        max_length=125,
        null=True,
        blank=True)

    preventative_action_datetime = models.DateTimeField(
        verbose_name='Preventative action date and time:',
        validators=[date_not_future],
        null=True,
        blank=True)

    preventative_action = models.CharField(
        verbose_name='Preventative action taken:',
        max_length=125,
        null=True,
        blank=True)

    action_required = models.CharField(
        max_length=25,
        choices=ACTION_REQUIRED,
        null=True,
        blank=True)

    history = HistoricalRecords()

    class Meta(CrfModelMixin.Meta):
        app_label = 'ambition_subject'
        verbose_name = 'Protocol Deviation Violation'
        verbose_name_plural = 'Protocol Deviation Violations'
