from django.apps import apps as django_apps
from django.test import TestCase, tag
from edc_constants.constants import FEMALE, YES, ABNORMAL, NORMAL, NO, MALE, NOT_APPLICABLE
from edc_form_validators.base_form_validator import NOT_APPLICABLE_ERROR
from model_mommy import mommy

from ..models import SubjectScreening


class TestSubjectScreening(TestCase):

    def setUp(self):
        django_apps.app_configs[
            'ambition_subject'].screening_age_adult_upper = 99
        django_apps.app_configs[
            'ambition_subject'].screening_age_adult_lower = 18

    def test_eligible_with_default_recipe_criteria(self):
        subject_screening = mommy.make_recipe(
            'ambition_subject.subjectscreening')
        self.assertTrue(subject_screening.eligible)
        self.assertTrue(subject_screening.gender, MALE)
        self.assertTrue(subject_screening.pregnancy, NOT_APPLICABLE)
        self.assertTrue(subject_screening.breast_feeding, NOT_APPLICABLE_ERROR)

    def test_subject_invalid_age_in_years_lower(self):
        """Asserts mommy recipe default criteria is eligible.
        """
        subject_screening = mommy.prepare_recipe(
            'ambition_subject.subjectscreening', age_in_years=17)
#         subject_screening.verify_eligibility()
        self.assertFalse(subject_screening.eligible)

    def test_subject_age_minor_invalid_reason(self):
        options = {'age_in_years': 17}
        subject_screening = mommy.make_recipe(
            'ambition_subject.subjectscreening', **options)
        self.assertFalse(subject_screening.eligible)
        self.assertIn(
            subject_screening.reasons_ineligible, 'age<18.')

    def test_subject_age_valid_no_reason(self):
        options = {'age_in_years': 18}
        subject_screening = mommy.make_recipe(
            'ambition_subject.subjectscreening', **options)
        self.assertTrue(subject_screening.eligible)
        self.assertEqual(subject_screening.reasons_ineligible, '')

    def test_subject_ineligible_female_pregnant(self):
        """Assert not eligible if pregnant.
        """
        options = {'gender': FEMALE, 'pregnancy': YES}
        subject_screening = mommy.make_recipe(
            'ambition_subject.subjectscreening', **options)
        self.assertFalse(subject_screening.eligible)

    def test_subject_ineligible_previous_adverse_drug_reaction(self):
        """Assert eligibility of a participant with a previous adverse
        drug reaction.
        """
        options = {'previous_drug_reaction': YES}
        subject_screening = mommy.make_recipe(
            'ambition_subject.subjectscreening', **options)
        self.assertFalse(subject_screening.eligible)

    def test_subject_ineligible_taking_concomitant_medication(self):
        """Test eligibility of a participant taking concomitant
        medication.
        """
        options = {'contraindicated_meds': YES}
        subject_screening = mommy.make_recipe(
            'ambition_subject.subjectscreening', **options)
        self.assertFalse(subject_screening.eligible)

    def test_subject_ineligible_took_two_days_amphotricin_b(self):
        """Test eligibility of a participant that received two days
        amphotricin_b before screening.
        """
        options = {'received_amphotericin': YES}
        subject_screening = mommy.make_recipe(
            'ambition_subject.subjectscreening', **options)
        self.assertFalse(subject_screening.eligible)

    def test_subject_ineligible_took_received_fluconazole(self):
        """Assert eligibility of a participant that received two days
        fluconazole before screening.
        """
        subject_screening = mommy.make_recipe(
            'ambition_subject.subjectscreening',
            received_fluconazole=YES)
        self.assertFalse(subject_screening.eligible)

    def test_eligible_mental_status_normal(self):
        subject_screening = mommy.make_recipe(
            'ambition_subject.subjectscreening')
        self.assertIn(subject_screening.mental_status, NORMAL)
        self.assertTrue(subject_screening.eligible)

    def test_ineligible_mental_abnormal(self):
        subject_screening = mommy.make_recipe(
            'ambition_subject.subjectscreening',
            mental_status=ABNORMAL, consent_ability=NO)
        self.assertFalse(subject_screening.eligible)

    def test_ineligible_not_willing_to_hiv_test(self):
        subject_screening = mommy.make_recipe(
            'ambition_subject.subjectscreening',
            will_hiv_test=NO)
        self.assertFalse(subject_screening.eligible)

    def test_eligible_willing_to_hiv_test(self):
        subject_screening = mommy.make_recipe(
            'ambition_subject.subjectscreening',
            will_hiv_test=YES)
        self.assertTrue(subject_screening.eligible)

    def test_ineligible_mental_status_abnormal(self):
        subject_screening = mommy.make_recipe(
            'ambition_subject.subjectscreening',
            mental_status=ABNORMAL)
        self.assertFalse(subject_screening.eligible)

    def test_ineligible_without_consent_ability(self):
        subject_screening = mommy.make_recipe(
            'ambition_subject.subjectscreening',
            consent_ability=NO)
        self.assertTrue(subject_screening.eligible)

    def test_ineligible_if_breastfeeding(self):
        subject_screening = mommy.make_recipe(
            'ambition_subject.subjectscreening',
            gender=FEMALE, pregnancy=NO, breast_feeding=YES)
        self.assertFalse(subject_screening.eligible)

    def test_eligible_if_not_breastfeeding(self):
        subject_screening = mommy.make_recipe(
            'ambition_subject.subjectscreening',
            gender=FEMALE, pregnancy=NO, breast_feeding=NO)
        self.assertTrue(subject_screening.eligible)

    def test_ineligible_if_pregnant(self):
        subject_screening = mommy.make_recipe(
            'ambition_subject.subjectscreening',
            gender=FEMALE, pregnancy=YES)
        self.assertFalse(subject_screening.eligible)

    def test_screening_id_created(self):
        subject_screening = mommy.make_recipe(
            'ambition_subject.subjectscreening',
            age_in_years=18)
        self.assertTrue(subject_screening.eligible)
        # requery
        subject_screening = SubjectScreening.objects.get(
            pk=subject_screening.id)
        self.assertIsNotNone(subject_screening.screening_identifier)

    def test_screening_id_unchanged_on_resave(self):
        """Test subject screening id is not changed when resaving.
        """
        obj = mommy.make_recipe(
            'ambition_subject.subjectscreening',
            age_in_years=18)
        self.assertTrue(obj.eligible)
        # resave
        obj.save()
        # requery
        subject_screening = SubjectScreening.objects.get(pk=obj.id)
        screening_identifier = subject_screening.screening_identifier
        self.assertEqual(obj.screening_identifier, screening_identifier)
