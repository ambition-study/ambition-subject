import re

from ambition_prn.models import OnSchedule
from ambition_rando.tests import AmbitionTestCaseMixin
from django.core.exceptions import ObjectDoesNotExist
from django.test import TestCase, tag
from django.test.utils import override_settings
from edc_base.utils import get_utcnow
from edc_constants.constants import UUID_PATTERN
from edc_registration.models import RegisteredSubject
from model_mommy import mommy

from ..models import SubjectConsent


@override_settings(SITE_ID='10')
class TestSubjectConsent(AmbitionTestCaseMixin, TestCase):

    def setUp(self):
        self.subject_screening = mommy.make_recipe(
            'ambition_screening.subjectscreening')

    def test_allocated_subject_identifier(self):
        """Test consent successfully allocates subject identifier on
        save.
        """
        options = {
            'screening_identifier': self.subject_screening.screening_identifier,
            'consent_datetime': get_utcnow, }
        mommy.make_recipe('ambition_subject.subjectconsent', **options)
        self.assertFalse(
            re.match(
                UUID_PATTERN,
                SubjectConsent.objects.all()[0].subject_identifier))

    def test_consent_creates_registered_subject(self):
        options = {
            'screening_identifier': self.subject_screening.screening_identifier,
            'consent_datetime': get_utcnow, }
        self.assertEquals(RegisteredSubject.objects.all().count(), 0)
        mommy.make_recipe('ambition_subject.subjectconsent', **options)
        self.assertEquals(RegisteredSubject.objects.all().count(), 1)

#     def test_screening_datetime_updated_on_registered_subject(self):
#         options = {
#             'screening_identifier': self.subject_screening.screening_identifier,
#             'consent_datetime': get_utcnow, }
#         self.assertEquals(RegisteredSubject.objects.all().count(), 0)
#         subject_consent = mommy.make_recipe('ambition_subject.subjectconsent', **options)
#         registered_subject = RegisteredSubject.objects.get(
#             subject_identifier=subject_consent.subject_identifier)
#         self.assertEquals(
#             registered_subject.screening_datetime, self.subject_screening.report_datetime)


    def test_onschedule_created_on_consent(self):
        subject_consent = mommy.make_recipe(
            'ambition_subject.subjectconsent',
            consent_datetime=get_utcnow,
            screening_identifier=self.subject_screening.screening_identifier)

        try:
            OnSchedule.objects.get(
                subject_identifier=subject_consent.subject_identifier)
        except ObjectDoesNotExist:
            self.fail('ObjectDoesNotExist was unexpectedly raised.')
