from datetime import datetime
from edc_appointment.apps import AppConfig as BaseEdcAppointmentAppConfig
from edc_base.apps import AppConfig as BaseEdcBaseAppConfig
from edc_base.utils import get_utcnow
from edc_base_test.apps import AppConfig as BaseEdcBaseTestAppConfig
from edc_consent.apps import AppConfig as BaseEdcConsentAppConfig
from edc_constants.constants import FAILED_ELIGIBILITY
from edc_device.apps import AppConfig as BaseEdcDeviceAppConfig
from edc_device.constants import CENTRAL_SERVER
from edc_identifier.apps import AppConfig as BaseEdcIdentifierAppConfig
from edc_lab.apps import AppConfig as BaseEdcLabAppConfig
from edc_label.apps import AppConfig as BaseEdcLabelAppConfig
from edc_metadata.apps import AppConfig as BaseEdcMetadataAppConfig
from edc_protocol.apps import AppConfig as BaseEdcProtocolAppConfig, SubjectType, Cap
from edc_sync.apps import AppConfig as BaseEdcSyncAppConfig
from edc_sync_files.apps import AppConfig as BaseEdcSyncFilesAppConfig
from edc_timepoint.apps import AppConfig as BaseEdcTimepointAppConfig
from edc_timepoint.timepoint import Timepoint
from edc_visit_tracking.apps import AppConfig as BaseEdcVisitTrackingAppConfig
from edc_visit_tracking.constants import MISSED_VISIT
from edc_visit_tracking.constants import SCHEDULED, UNSCHEDULED, LOST_VISIT
import os

from dateutil.relativedelta import MO, TU, WE, TH, FR, SA, SU
from dateutil.tz import gettz
from django.apps import AppConfig as DjangoApponfig
from django.conf import settings
from edc_appointment.appointment_config import AppointmentConfig
from edc_facility import Facility


class AppConfig(DjangoApponfig):
    name = 'ambition_subject'
    admin_site_name = 'ambition_subject_admin'

    screening_age_adult_upper = 99
    screening_age_adult_lower = 18
    include_in_administration_section = False

    def ready(self):
        from .models.signals import subject_consent_on_post_save

        # if 'migrate' not in sys.argv and 'makemigrations' not in sys.argv:
        #    load_randomization()


if settings.APP_NAME == 'ambition_subject':
    class EdcProtocolAppConfig(BaseEdcProtocolAppConfig):
        protocol = 'BHP092'
        protocol_number = '092'
        protocol_name = 'Ambition'
        protocol_title = ''
        subject_types = [
            SubjectType('subject', 'Research Subject',
                        Cap(model_name='ambition_subject.subjectconsent', max_subjects=9999)),
        ]
        study_open_datetime = datetime(
            2016, 12, 31, 0, 0, 0, tzinfo=gettz('UTC'))
        study_close_datetime = datetime(
            2019, 12, 31, 0, 0, 0, tzinfo=gettz('UTC'))

        @property
        def site_name(self):
            return 'Gaborone'

        @property
        def site_code(self):
            return '40'

    class EdcLabAppConfig(BaseEdcLabAppConfig):
        base_template_name = 'ambition/base.html'
        requisition_model = 'ambition_subject.subjectrequisition'
        result_model = 'edc_lab.result'

        @property
        def site_name(self):
            return 'Gaborone'

        @property
        def site_code(self):
            return '40'

    class EdcBaseAppConfig(BaseEdcBaseAppConfig):
        project_name = 'Ambition'
        institution = 'Botswana-Harvard AIDS Institute'
        copyright = '2017-{}'.format(get_utcnow().year)
        license = None

    class EdcBaseTestAppConfig(BaseEdcBaseTestAppConfig):
        consent_model = 'ambition_subject.subjectconsent'

    class EdcConsentAppConfig(BaseEdcConsentAppConfig):
        pass

    class EdcDeviceAppConfig(BaseEdcDeviceAppConfig):
        device_role = CENTRAL_SERVER
        device_id = '99'

    class EdcVisitTrackingAppConfig(BaseEdcVisitTrackingAppConfig):
        visit_models = {
            'ambition_subject': ('subject_visit', 'ambition_subject.subjectvisit')}

    class EdcIdentifierAppConfig(BaseEdcIdentifierAppConfig):
        identifier_prefix = '092'

    class EdcMetadataAppConfig(BaseEdcMetadataAppConfig):
        reason_field = {'ambition_subject.subjectvisit': 'reason'}
        create_on_reasons = [SCHEDULED, UNSCHEDULED]
        delete_on_reasons = [LOST_VISIT, FAILED_ELIGIBILITY, MISSED_VISIT]

    class EdcAppointmentAppConfig(BaseEdcAppointmentAppConfig):
        app_label = 'ambition_subject'
        default_appt_type = 'hospital'
        configurations = [
            AppointmentConfig(
                model='ambition_subject.appointment',
                related_visit_model='ambition_subject.subjectvisit')
        ]
        facilities = {
            'clinic': Facility(
                name='clinic', days=[MO, TU, WE, TH, FR, SA, SU],
                slots=[99999, 99999, 99999, 99999, 99999, 99999, 99999])}

    class EdcTimepointAppConfig(BaseEdcTimepointAppConfig):
        timepoints = [
            Timepoint(
                model='ambition_subject.appointment',
                datetime_field='appt_datetime',
                status_field='appt_status',
                closed_status='DONE'
            ),
            Timepoint(
                model='ambition_subject.historicalappointment',
                datetime_field='appt_datetime',
                status_field='appt_status',
                closed_status='DONE'
            ),
        ]

    class EdcSyncAppConfig(BaseEdcSyncAppConfig):
        edc_sync_files_using = True
        role = CENTRAL_SERVER

    class EdcLabelAppConfig(BaseEdcLabelAppConfig):
        template_folder = os.path.join(
            settings.STATIC_ROOT, 'ambition', 'label_templates')

    class EdcSyncFilesAppConfig(BaseEdcSyncFilesAppConfig):
        edc_sync_files_using = True
        role = CENTRAL_SERVER
