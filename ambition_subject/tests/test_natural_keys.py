from ambition_rando.tests import AmbitionTestCaseMixin
from ambition_visit_schedule import DAY1, DAY3, DAY5, DAY7, DAY14, DAY12
from ambition_visit_schedule import DAY10, WEEK4, WEEK6, WEEK8, WEEK10, WEEK16
from django.test import TestCase, tag
from django.test.utils import override_settings
from edc_appointment.models import Appointment
from edc_base.utils import get_utcnow
from edc_metadata.tests import CrfTestHelper
from edc_sync.tests import SyncTestHelper
from edc_visit_tracking.constants import SCHEDULED
from edc_facility.import_holidays import import_holidays
from model_mommy import mommy

from ..models import SubjectVisit


@override_settings(SITE_ID='10')
class TestNaturalKey(AmbitionTestCaseMixin, TestCase):

    sync_test_helper = SyncTestHelper()
    crf_test_helper = CrfTestHelper()

    def setUp(self):
        import_holidays()
        self.visit_codes = [DAY1, DAY3, DAY5, DAY7, DAY14, DAY12,
                            DAY10, WEEK4, WEEK6, WEEK8, WEEK10, WEEK16]

    def test_natural_key_attrs(self):
        self.sync_test_helper.sync_test_natural_key_attr(
            'ambition_subject')

    def test_get_by_natural_key_attr(self):
        self.sync_test_helper.sync_test_get_by_natural_key_attr(
            'ambition_subject')

    def complete_all_subject_visits(self):
        screening = mommy.make_recipe('ambition_screening.subjectscreening',
                                      report_datetime=get_utcnow())
        consent = mommy.make_recipe('ambition_subject.subjectconsent',
                                    consent_datetime=get_utcnow(),
                                    screening_identifier=screening.screening_identifier)
        self.subject_identifier = consent.subject_identifier

        for appointment in Appointment.objects.all().order_by('timepoint'):
            mommy.make_recipe(
                'ambition_subject.subjectvisit',
                appointment=appointment,
                subject_identifier=consent.subject_identifier,
                reason=SCHEDULED)

    def test_sync_test_natural_keys(self):
        complete_required_crfs = {}
        visit = self.complete_all_subject_visits()
        for visit_code in self.visit_codes:
            visit = SubjectVisit.objects.get(
                appointment=Appointment.objects.get(visit_code=visit_code))
            complete_required_crfs.update({
                visit.visit_code: self.crf_test_helper.complete_required_crfs(
                    visit_code=visit.visit_code,
                    visit=visit,
                    subject_identifier=visit.subject_identifier)})
            self.sync_test_helper.sync_test_natural_keys(
                complete_required_crfs)

    def test_sync_deserialize(self):
        complete_required_crfs = {}
        visit = self.complete_all_subject_visits()
        for visit_code in self.visit_codes:
            visit = SubjectVisit.objects.get(
                appointment=Appointment.objects.get(visit_code=visit_code))
            complete_required_crfs.update({
                visit.visit_code: self.crf_test_helper.complete_required_crfs(
                    visit_code=visit.visit_code,
                    visit=visit,
                    subject_identifier=visit.subject_identifier)})
            self.sync_test_helper.sync_test_serializers_for_visit(
                complete_required_crfs)
