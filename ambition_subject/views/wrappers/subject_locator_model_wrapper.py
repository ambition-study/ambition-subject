from django.apps import apps as django_apps

from edc_model_wrapper.wrappers import ModelWrapper


class SubjectLocatorModelWrapper(ModelWrapper):

    model = 'ambition_subject.subjectlocator'

    admin_site_name = django_apps.get_app_config(
        'ambition_subject').admin_site_name

    next_url_name = django_apps.get_app_config(
        'ambition_subject').dashboard_url_name
    next_url_attrs = ['subject_identifier']
    url_instance_attrs = ['subject_identifier']
