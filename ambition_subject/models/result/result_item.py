from django.db import models
from django.db.models.deletion import PROTECT

from edc_base.model_mixins import BaseUuidModel
from edc_base.model_managers import HistoricalRecords
from edc_lab.model_mixins.result import ResultItemModelMixin

from .result import Result


class ResultItemManager(models.Manager):

    def get_by_natural_key(self, report_datetime, requisition_identifier):
        return self.get(
            report_datetime=report_datetime,
            requisition__requisition_identifier=requisition_identifier,)


class ResultItem(ResultItemModelMixin, BaseUuidModel):

    result = models.ForeignKey(Result, on_delete=PROTECT)

    objects = ResultItemManager()

    history = HistoricalRecords()

    def natural_key(self):
        return (self.report_datetime,) + self.result.natural_key()
    natural_key.dependencies = ['ambition_subject.result']

    class Meta:
        app_label = 'ambition_subject'
