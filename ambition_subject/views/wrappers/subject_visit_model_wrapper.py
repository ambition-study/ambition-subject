from django.apps import apps as django_apps

from edc_model_wrapper import ModelWrapper


class SubjectVisitModelWrapper(ModelWrapper):

    model = 'ambition_subject.subjectvisit'
    next_url_name = django_apps.get_app_config(
        'ambition_subject').dashboard_url_name
    next_url_attrs = ['subject_identifier', 'appointment']

    @property
    def appointment(self):
        return self.object.appointment.id
