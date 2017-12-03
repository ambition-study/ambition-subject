from ambition_rando.import_randomization_list import import_randomization_list
from ambition_subject.models.subject_visit import SubjectVisit
from django.test import TestCase, tag
from edc_appointment.models import Appointment
from edc_base.utils import get_utcnow
from edc_constants.constants import YES, NO
from edc_metadata.constants import NOT_REQUIRED, REQUIRED
from edc_metadata.models import CrfMetadata
from edc_visit_tracking.constants import SCHEDULED
from model_mommy import mommy


class TestSubjectRules(TestCase):

    def setUp(self):
        import_randomization_list(verbose=False)
        screening = mommy.make_recipe('ambition_subject.subjectscreening',
                                      report_datetime=get_utcnow())
        self.consent = mommy.make_recipe(
            'ambition_subject.subjectconsent',
            consent_datetime=get_utcnow(),
            screening_identifier=screening.screening_identifier)

        self.visit_code = '1070'

        for appointment in Appointment.objects.all().order_by('timepoint'):
            self.subject_visit = mommy.make_recipe(
                'ambition_subject.subjectvisit',
                appointment=appointment,
                reason=SCHEDULED)
            if appointment.visit_code == self.visit_code:
                break

    def test_death_report_required_included_in_error(self):
        self.assertEqual(
            CrfMetadata.objects.get(
                model='ambition_subject.deathreport',
                subject_identifier=self.consent.subject_identifier,
                visit_code='1070').entry_status,
            NOT_REQUIRED)

        mommy.make_recipe(
            'ambition_subject.adverseevent',
            subject_visit=self.subject_visit,
            ae_grade='grade_5')

        self.assertEqual(
            CrfMetadata.objects.get(
                model='ambition_subject.deathreport',
                subject_identifier=self.consent.subject_identifier,
                visit_code='1070').entry_status,
            REQUIRED)

    def test_protocol_deviation_violation_required_included_in_error(self):
        self.assertEqual(
            CrfMetadata.objects.get(
                model='ambition_subject.protocoldeviationviolation',
                subject_identifier=self.consent.subject_identifier,
                visit_code='1070').entry_status,
            NOT_REQUIRED)

        mommy.make_recipe(
            'ambition_subject.studyterminationconclusion',
            subject_visit=self.subject_visit,
            termination_reason='included_in_error')

        self.assertEqual(
            CrfMetadata.objects.get(
                model='ambition_subject.protocoldeviationviolation',
                subject_identifier=self.consent.subject_identifier,
                visit_code='1070').entry_status,
            REQUIRED)

    def test_blood_result_required_prn_form(self):
        self.assertEqual(
            CrfMetadata.objects.get(
                model='ambition_subject.bloodresult',
                subject_identifier=self.consent.subject_identifier,
                visit_code='1070').entry_status,
            NOT_REQUIRED)

        mommy.make_recipe(
            'ambition_subject.prnmodel',
            subject_visit=self.subject_visit,
            blood_result=YES)

        self.assertEqual(
            CrfMetadata.objects.get(
                model='ambition_subject.bloodresult',
                subject_identifier=self.consent.subject_identifier,
                visit_code='1070').entry_status,
            REQUIRED)

    def test_adverse_event_required(self):
        self.assertEqual(
            CrfMetadata.objects.get(
                model='ambition_subject.adverseevent',
                subject_identifier=self.consent.subject_identifier,
                visit_code='1070').entry_status,
            NOT_REQUIRED)

        mommy.make_recipe(
            'ambition_subject.prnmodel',
            subject_visit=self.subject_visit,
            adverse_event=YES)

        self.assertEqual(
            CrfMetadata.objects.get(
                model='ambition_subject.adverseevent',
                subject_identifier=self.consent.subject_identifier,
                visit_code='1070').entry_status,
            REQUIRED)

    def test_adverse_event_tmg_required(self):
        self.assertEqual(
            CrfMetadata.objects.get(
                model='ambition_subject.adverseeventtmg',
                subject_identifier=self.consent.subject_identifier,
                visit_code='1070').entry_status,
            NOT_REQUIRED)

        mommy.make_recipe(
            'ambition_subject.prnmodel',
            subject_visit=self.subject_visit,
            adverse_event_tmg=YES)

        self.assertEqual(
            CrfMetadata.objects.get(
                model='ambition_subject.adverseeventtmg',
                subject_identifier=self.consent.subject_identifier,
                visit_code='1070').entry_status,
            REQUIRED)

    def test_adverse_event_followup_required(self):
        self.assertEqual(
            CrfMetadata.objects.get(
                model='ambition_subject.adverseeventfollowup',
                subject_identifier=self.consent.subject_identifier,
                visit_code='1070').entry_status,
            NOT_REQUIRED)

        mommy.make_recipe(
            'ambition_subject.prnmodel',
            subject_visit=self.subject_visit,
            adverse_event_followup=YES)

        self.assertEqual(
            CrfMetadata.objects.get(
                model='ambition_subject.adverseeventfollowup',
                subject_identifier=self.consent.subject_identifier,
                visit_code='1070').entry_status,
            REQUIRED)

    def test_microbiology_required(self):
        self.assertEqual(
            CrfMetadata.objects.get(
                model='ambition_subject.microbiology',
                subject_identifier=self.consent.subject_identifier,
                visit_code='1070').entry_status,
            NOT_REQUIRED)
        mommy.make_recipe(
            'ambition_subject.prnmodel',
            subject_visit=self.subject_visit,
            microbiology=YES)
        self.assertEqual(
            CrfMetadata.objects.get(
                model='ambition_subject.microbiology',
                subject_identifier=self.consent.subject_identifier,
                visit_code='1070').entry_status,
            REQUIRED)

    def test_radiology_required(self):
        self.assertEqual(
            CrfMetadata.objects.get(
                model='ambition_subject.radiology',
                subject_identifier=self.consent.subject_identifier,
                visit_code='1070').entry_status,
            NOT_REQUIRED)
        mommy.make_recipe(
            'ambition_subject.prnmodel',
            subject_visit=self.subject_visit,
            radiology=YES)
        self.assertEqual(
            CrfMetadata.objects.get(
                model='ambition_subject.radiology',
                subject_identifier=self.consent.subject_identifier,
                visit_code='1070').entry_status,
            REQUIRED)

    def test_lumbar_puncture_required(self):
        self.assertEqual(
            CrfMetadata.objects.get(
                model='ambition_subject.lumbarpuncturecsf',
                subject_identifier=self.consent.subject_identifier,
                visit_code='1070').entry_status,
            NOT_REQUIRED)
        mommy.make_recipe(
            'ambition_subject.prnmodel',
            subject_visit=self.subject_visit,
            lumbar_puncture=YES)
        self.assertEqual(
            CrfMetadata.objects.get(
                model='ambition_subject.lumbarpuncturecsf',
                subject_identifier=self.consent.subject_identifier,
                visit_code='1070').entry_status,
            REQUIRED)

    def test_recurrence_symptom_required(self):
        self.assertEqual(
            CrfMetadata.objects.get(
                model='ambition_subject.recurrencesymptom',
                subject_identifier=self.consent.subject_identifier,
                visit_code='1070').entry_status,
            NOT_REQUIRED)
        mommy.make_recipe(
            'ambition_subject.prnmodel',
            subject_visit=self.subject_visit,
            recurrence_symptom=YES)
        self.assertEqual(
            CrfMetadata.objects.get(
                model='ambition_subject.recurrencesymptom',
                subject_identifier=self.consent.subject_identifier,
                visit_code='1070').entry_status,
            REQUIRED)

    def test_protocol_deviation_required(self):
        self.assertEqual(
            CrfMetadata.objects.get(
                model='ambition_subject.protocoldeviationviolation',
                subject_identifier=self.consent.subject_identifier,
                visit_code='1070').entry_status,
            NOT_REQUIRED)
        mommy.make_recipe(
            'ambition_subject.prnmodel',
            subject_visit=self.subject_visit,
            protocol_deviation=YES)
        self.assertEqual(
            CrfMetadata.objects.get(
                model='ambition_subject.protocoldeviationviolation',
                subject_identifier=self.consent.subject_identifier,
                visit_code='1070').entry_status,
            REQUIRED)

    def test_death_report_required(self):
        self.assertEqual(
            CrfMetadata.objects.get(
                model='ambition_subject.deathreport',
                subject_identifier=self.consent.subject_identifier,
                visit_code='1070').entry_status,
            NOT_REQUIRED)
        mommy.make_recipe(
            'ambition_subject.prnmodel',
            subject_visit=self.subject_visit,
            death_report=YES)
        self.assertEqual(
            CrfMetadata.objects.get(
                model='ambition_subject.deathreport',
                subject_identifier=self.consent.subject_identifier,
                visit_code='1070').entry_status,
            REQUIRED)

    def test_recurrence_symptom_required_from_adverse_event(self):
        self.assertEqual(
            CrfMetadata.objects.get(
                model='ambition_subject.recurrencesymptom',
                subject_identifier=self.consent.subject_identifier,
                visit_code='1070').entry_status,
            NOT_REQUIRED)

        mommy.make_recipe(
            'ambition_subject.adverseevent',
            subject_visit=self.subject_visit,
            ae_cm_recurrence=YES)

        self.assertEqual(
            CrfMetadata.objects.get(
                model='ambition_subject.recurrencesymptom',
                subject_identifier=self.consent.subject_identifier,
                visit_code='1070').entry_status,
            REQUIRED)

    def test_death_report_required_on_prn(self):
        appointment = Appointment.objects.get(
            subject_identifier=self.consent.subject_identifier,
            visit_code='1112')
        self.subject_visit = mommy.make_recipe(
            'ambition_subject.subjectvisit',
            appointment=appointment,
            reason=SCHEDULED)
        self.assertEqual(
            CrfMetadata.objects.get(
                model='ambition_subject.deathreport',
                subject_identifier=self.consent.subject_identifier,
                visit_code='1112').entry_status,
            NOT_REQUIRED)

        mommy.make_recipe(
            'ambition_subject.week16',
            subject_visit=self.subject_visit,
            patient_alive=NO)

        self.assertEqual(
            CrfMetadata.objects.get(
                model='ambition_subject.deathreport',
                subject_identifier=self.consent.subject_identifier,
                visit_code='1112').entry_status,
            REQUIRED)

    def test_death_report_required_on_prn_1(self):
        appointment = Appointment.objects.get(
            subject_identifier=self.consent.subject_identifier,
            visit_code='1112')
        self.subject_visit = mommy.make_recipe(
            'ambition_subject.subjectvisit',
            appointment=appointment,
            reason=SCHEDULED)
        self.assertEqual(
            CrfMetadata.objects.get(
                model='ambition_subject.deathreport',
                subject_identifier=self.consent.subject_identifier,
                visit_code='1112').entry_status,
            NOT_REQUIRED)

        week16 = mommy.make_recipe(
            'ambition_subject.week16',
            subject_visit=self.subject_visit,
            patient_alive=YES)

        self.assertEqual(
            CrfMetadata.objects.get(
                model='ambition_subject.deathreport',
                subject_identifier=self.consent.subject_identifier,
                visit_code='1112').entry_status,
            NOT_REQUIRED)

        week16.patient_alive = NO
        week16.save()
        self.assertEqual(
            CrfMetadata.objects.get(
                model='ambition_subject.deathreport',
                subject_identifier=self.consent.subject_identifier,
                visit_code='1112').entry_status,
            REQUIRED)

    @tag('recurrence_form')
    def test_recurrence_form(self):
        appointment = Appointment.objects.get(
            subject_identifier=self.consent.subject_identifier,
            visit_code='1005')
        self.subject_visit = SubjectVisit.objects.get(
            appointment=appointment)

        mommy.make_recipe(
            'ambition_subject.adverseevent',
            subject_visit=self.subject_visit,
            ae_cm_recurrence=YES)

        self.assertEqual(
            CrfMetadata.objects.get(
                model='ambition_subject.recurrencesymptom',
                subject_identifier=self.consent.subject_identifier,
                visit_code='1005').entry_status,
            REQUIRED)

    def test_recurrence_form_1(self):
        appointment = Appointment.objects.get(
            subject_identifier=self.consent.subject_identifier,
            visit_code='1005')
        self.subject_visit = SubjectVisit.objects.get(
            appointment=appointment)

        mommy.make_recipe(
            'ambition_subject.adverseevent',
            subject_visit=self.subject_visit,
            ae_cm_recurrence=NO)

        self.assertEqual(
            CrfMetadata.objects.get(
                model='ambition_subject.recurrencesymptom',
                subject_identifier=self.consent.subject_identifier,
                visit_code='1005').entry_status,
            NOT_REQUIRED)

    def test_recurrence_form_2(self):
        appointment = Appointment.objects.get(
            subject_identifier=self.consent.subject_identifier,
            visit_code='1005')
        self.subject_visit = SubjectVisit.objects.get(
            appointment=appointment)

        mommy.make_recipe(
            'ambition_subject.adverseevent',
            subject_visit=self.subject_visit,
            ae_cm_recurrence=NO)

        mommy.make_recipe(
            'ambition_subject.prnmodel',
            subject_visit=self.subject_visit,
            recurrence_symptom=NO)

        self.assertEqual(
            CrfMetadata.objects.get(
                model='ambition_subject.recurrencesymptom',
                subject_identifier=self.consent.subject_identifier,
                visit_code='1005').entry_status,
            NOT_REQUIRED)

    def test_recurrence_form_3(self):
        appointment = Appointment.objects.get(
            subject_identifier=self.consent.subject_identifier,
            visit_code='1005')
        self.subject_visit = SubjectVisit.objects.get(
            appointment=appointment)

        mommy.make_recipe(
            'ambition_subject.adverseevent',
            subject_visit=self.subject_visit,
            ae_cm_recurrence=NO)

        mommy.make_recipe(
            'ambition_subject.prnmodel',
            subject_visit=self.subject_visit,
            recurrence_symptom=YES)

        self.assertEqual(
            CrfMetadata.objects.get(
                model='ambition_subject.recurrencesymptom',
                subject_identifier=self.consent.subject_identifier,
                visit_code='1005').entry_status,
            REQUIRED)

    @tag('result_rule')
    def test_blood_result_rule_not_required(self):
        appointment = Appointment.objects.get(
            subject_identifier=self.consent.subject_identifier,
            visit_code='1000')
        self.subject_visit = SubjectVisit.objects.get(
            appointment=appointment)

        mommy.make_recipe(
            'ambition_subject.bloodresult',
            subject_visit=self.subject_visit,
            absolute_neutrophil=55,
            alt=199,
            platelets=5451)

        self.assertEqual(
            CrfMetadata.objects.get(
                model='ambition_subject.subjectoffstudy',
                subject_identifier=self.consent.subject_identifier,
                visit_code='1000').entry_status,
            NOT_REQUIRED)

    def test_blood_result_rule_required(self):
        appointment = Appointment.objects.get(
            subject_identifier=self.consent.subject_identifier,
            visit_code='1000')
        self.subject_visit = SubjectVisit.objects.get(
            appointment=appointment)

        mommy.make_recipe(
            'ambition_subject.bloodresult',
            subject_visit=self.subject_visit,
            absolute_neutrophil=55,
            alt=201,
            platelets=5451)

        self.assertEqual(
            CrfMetadata.objects.get(
                model='ambition_subject.subjectoffstudy',
                subject_identifier=self.consent.subject_identifier,
                visit_code='1000').entry_status,
            REQUIRED)

    def test_medical_expenses_two_required(self):
        appointment = Appointment.objects.get(
            subject_identifier=self.consent.subject_identifier,
            visit_code='1000')
        self.subject_visit = SubjectVisit.objects.get(
            appointment=appointment)

        mommy.make_recipe(
            'ambition_subject.medicalexpenses',
            subject_visit=self.subject_visit,
            care_before_hospital=YES)

        self.assertEqual(
            CrfMetadata.objects.get(
                model='ambition_subject.medicalexpensestwo',
                subject_identifier=self.consent.subject_identifier,
                visit_code='1000').entry_status,
            REQUIRED)
