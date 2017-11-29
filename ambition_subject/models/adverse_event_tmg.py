from django.db import models
from django.db.models.deletion import PROTECT
from edc_base.model_fields import OtherCharField
from edc_base.model_managers import HistoricalRecords
from edc_base.model_mixins import BaseUuidModel
from edc_base.model_validators import date_not_future
from edc_identifier.model_mixins import NonUniqueSubjectIdentifierFieldMixin
from edc_base.utils import get_utcnow

from .list_models import AEClassification
from .adverse_event import AdverseEvent


class AdverseEventTMG(NonUniqueSubjectIdentifierFieldMixin, BaseUuidModel):

    adverse_event = models.ForeignKey(AdverseEvent, on_delete=PROTECT)

    report_datetime = models.DateTimeField(
        verbose_name="Report Date and Time",
        default=get_utcnow)

    ae_received_datetime = models.DateTimeField(
        blank=True,
        null=True,
        validators=[date_not_future],
        verbose_name='Date and time AE form received:')

    clinical_review_datetime = models.DateTimeField(
        blank=True,
        null=True,
        verbose_name='Date and time of Clinical Review: ')

    investigator_comments = models.TextField(
        blank=True,
        null=True,
        verbose_name='Investigator Comments:')

    ae_classification = models.ManyToManyField(
        AEClassification,
        blank=True,
        verbose_name='Classification of AE (Tick all that apply):')

    ae_classification_other = OtherCharField(
        verbose_name='If Other, Specify',
        max_length=250,
        blank=True,
        null=True)

    ae_description = models.TextField(
        blank=True,
        null=True,
        verbose_name='Description of AE:')

    officials_notified = models.DateTimeField(
        blank=True,
        null=True,
        validators=[date_not_future],
        verbose_name='Date and time Regulatory authorities notified (SUSARs)')

    investigator_returned = models.DateTimeField(
        blank=True,
        null=True,
        validators=[date_not_future],
        verbose_name=('Date and time form logged in data base and returned'
                      'to Local Investigator'))

    history = HistoricalRecords()

    def save(self, *args, **kwargs):
        self.subject_identifier = self.adverse_event.subject_identifier
        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Adverse Event TMG'
