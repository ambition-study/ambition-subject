from django.core.validators import MinValueValidator
from django.db import models

from edc_base.model_managers import HistoricalRecords
from edc_base.model_validators import date_not_future
from edc_constants.choices import YES_NO, YES_NO_UNKNOWN

from ..choices import (REASON_DRUG_MISSED, MEDICINES, GLASGOW_COMA_SCORE_EYES,
                       GLASGOW_COMA_SCORE_VERBAL, GLASGOW_COMA_SCORE_MOTOR)
from .list_models import Antibiotic, OtherDrug
from .model_mixins import CrfModelMixin


class Week2(CrfModelMixin):

    discharged = models.CharField(
        verbose_name='Discharged?',
        max_length=25,
        choices=YES_NO)

    discharge_datetime = models.DateTimeField(
        validators=[date_not_future],
        null=True,
        blank=True)

    died = models.CharField(
        verbose_name='Died?',
        max_length=25,
        choices=YES_NO)

    death_datetime = models.DateTimeField(
        validators=[date_not_future],
        null=True,
        blank=True)

    ambisome_start_datetime = models.DateTimeField(
        validators=[date_not_future])

    ambisome_stop_datetime = models.DateTimeField(
        validators=[date_not_future],
        null=True,
        blank=True)

    fluconazole_start_datetime = models.DateTimeField(
        validators=[date_not_future],
        null=True,
        blank=True)

    fluconazole_stop_datetime = models.DateTimeField(
        validators=[date_not_future],
        null=True,
        blank=True)

    drug_doses_missed = models.CharField(
        verbose_name='Were any drug doses missed?',
        max_length=25,
        null=True,
        blank=True,
        choices=YES_NO)

    ambisome_missed_doses = models.CharField(
        max_length=25,
        null=True,
        blank=True,
        choices=YES_NO)

    ambisome_missed_reason = models.CharField(
        verbose_name='Were any drug doses missed?',
        max_length=25,
        null=True,
        blank=True,
        choices=REASON_DRUG_MISSED)

    fluconazole_missed_doses = models.CharField(
        verbose_name='Were any drug doses missed?',
        max_length=25,
        choices=YES_NO)

    fluconazole_missed_reason = models.CharField(
        verbose_name='Were any drug doses missed?',
        max_length=25,
        blank=True,
        choices=REASON_DRUG_MISSED)

    other_drug = models.ManyToManyField(
        OtherDrug,
        verbose_name="Other drugs/interventions given during first 14 days",)

    antibiotic = models.ManyToManyField(
        Antibiotic,
        verbose_name="if antibiotics, select the ones given",)

    blood_received = models.CharField(
        verbose_name='Blood transfusion received?',
        max_length=25,
        choices=YES_NO)

    units = models.IntegerField(
        verbose_name='If yes, No. of units',
        validators=[MinValueValidator(1)],
        null=True,
        blank=True)

    hiv_status_pos = models.CharField(
        verbose_name='HIV positive?',
        max_length=25,
        choices=YES_NO,
        help_text="Confirm with patient")

    new_hiv_diagnosis = models.CharField(
        verbose_name='Is this a new HIV diagnosis?',
        max_length=25,
        choices=YES_NO_UNKNOWN)

    clinic_assessment = models.CharField(
        verbose_name='Clinical Assessment',
        max_length=25,
        null=True,
        help_text='Patient died before 2 week assesment',
        choices=YES_NO)

    headache = models.CharField(
        verbose_name='Headache',
        max_length=25,
        choices=YES_NO,
        help_text="Confirm with patient")

    temperature = models.FloatField(
        verbose_name='Temperature',
        null=True,
        blank=True,
        default=None)

    glasgow_coma_score = models.IntegerField(
        verbose_name='Glasgow Coma Score',
        null=True,
        blank=True)

    seizures_during_admission = models.CharField(
        verbose_name='Seizures during admission',
        max_length=25,
        choices=YES_NO)

    recent_seizure = models.CharField(
        verbose_name='Recent seizure (<72 hrs):',
        max_length=25,
        choices=YES_NO)

    behaviour_change = models.CharField(
        verbose_name='Behaviour change',
        max_length=25,
        choices=YES_NO)

    confusion = models.CharField(
        verbose_name='Confusion',
        max_length=25,
        choices=YES_NO)

    cn_palsy = models.CharField(
        verbose_name='CN palsy',
        max_length=25,
        choices=YES_NO)

    focal_neurology = models.CharField(
        verbose_name='Focal Neurology:',
        max_length=25,
        choices=YES_NO)

    weight = models.IntegerField(
        null=True,
        blank=True)

    medicines = models.CharField(
        verbose_name='Medicines on Day 14:',
        max_length=25,
        choices=MEDICINES)

    significant_diagnosis = models.CharField(
        verbose_name='Other significant diagnoses since enrolment?',
        max_length=25,
        choices=YES_NO)

    glasgow_coma_score_eyes = models.CharField(
        verbose_name='Glasgow Coma Score of eyes',
        max_length=25,
        choices=GLASGOW_COMA_SCORE_EYES)

    glasgow_coma_score_verbal = models.CharField(
        verbose_name='Glasgow Coma Score of verbal',
        max_length=25,
        choices=GLASGOW_COMA_SCORE_VERBAL)

    glasgow_coma_score_motor = models.CharField(
        verbose_name='Glasgow Coma Score of motor',
        max_length=25,
        choices=GLASGOW_COMA_SCORE_MOTOR)

    history = HistoricalRecords()

    class Meta(CrfModelMixin.Meta):
        app_label = 'ambition_subject'