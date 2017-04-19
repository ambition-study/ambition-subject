from django.apps import apps as django_apps
from django.core.exceptions import ObjectDoesNotExist

from edc_constants.constants import OTHER, UNKNOWN

list_data = {
    'ambition_subject.aeclassification': [
        ('anaemia', 'Anaemia'),
        ('thrombocytopenia', 'Thrombocytopenia'),
        ('diarrhoea', 'Diarrhoea'),
        ('thrombophlebitis', 'Renal impairment'),
        ('pneumonia', 'Pneumonia'),
        ('TB', 'TB'),
        ('hypokalaemia', 'Hypokalaemia'),
        ('bacteraemia/sepsis', 'Bacteraemia/sepsis'),
        ('neutropaenia', 'Neutropaenia'),
        ('CM_IRIS', 'CM IRIS'),
        ('respiratory_distress', 'Respiratory distress'),
        (OTHER, 'Other')
    ],
    'ambition_subject.antibiotics': [
        ('flucloxacillin', 'Flucloxacillin'),
        ('gentamicin', 'Gentamicin'),
        ('ceftriaxone', 'Ceftriaxone'),
        ('amoxicillin_ampicillin', 'Amoxicillin/Ampicillin'),
        ('doxycycline', 'Doxycycline'),
        ('erythromycin', 'Erythromycin'),
        ('ciprofloxacin', 'Ciprofloxacin'),
        (OTHER, ' OTHER, specify')
    ],
    'ambition_subject.meningitissymptoms': [
        ('headache', 'Headache'),
        ('vomiting', 'Vomiting'),
        ('fever', 'Fever'),
        ('seizures', 'Seizures'),
        ('neck_pain', 'Neck Pain'),
        (OTHER, 'Other')
    ],
    'ambition_subject.missedvisitreasons': [
        ('transportation_difficulty', 'Transportation difficulty'),
        ('severely_sick', 'Severely sick or other physical conditions'),
        ('discouraged_by_clinic_situation', 'Discouraged by clinic situation '
                                            '(long waits, rude clinicians)'),
        ('away_working_schooling', 'Away Working/Schooling'),
        ('away_visiting', 'Away Visiting'),
        ('forgot', 'Forgot about appointment for clinic visit'),
        ('not_given_an_appointment', 'Not given an appointment'),
        (OTHER, 'Other, specify;'),
        (UNKNOWN, 'Reason not known at time of completing this form')
    ],
    'ambition_subject.neurological': [
        ('meningismus', 'Meningismus'),
        ('papilloedema', 'Papilloedema'),
        ('focal_neurologic_deficit', 'Focal neurologic deficit'),
        ('CN_VI_palsy', 'Cranial Nerve VI palsy'),
        ('CN_III_palsy', 'Cranial Nerve III palsy'),
        ('CN_IV_palsy', 'Cranial Nerve IV palsy'),
        ('CN_VII_palsy', 'Cranial Nerve VII palsy'),
        ('CN_VIII_palsy', 'Cranial Nerve VIII palsy'),
        (OTHER, 'Other CN palsy'),
    ],
    'ambition_subject.otherdruglist': [
        ('antibiotics', 'Antibiotics'),
        ('k', 'K'),
        ('mg', 'Mg'),
        ('vitamins', 'Vitamins'),
        ('tmp_smx_Cotrimoxazole', 'TMP-SMX/Cotrimoxazole'),
        ('anti_convulsants', 'Anti convulsants'),
        (OTHER, ' OTHER, specify')
    ],
    'ambition_subject.significantnewdiagnoses': [
        ('tb_pulmonary', 'TB pulmonary'),
        ('kaposi_sarcoma', 'Kaposi’s sarcoma'),
        ('bacteraemia', 'Bacteraemia'),
        ('diarrhoeal_wasting', 'Diarrhoeal wasting'),
        ('tb_extra_pulmonary', 'TB extra-pulmonary'),
        ('malaria', 'Malaria'),
        ('bacterial_pneumonia', 'Bacterial pneumonia'),
        (OTHER, 'Other, please specify:'), ],
    'ambition_subject.symptoms': [
        ('headache', 'Headache'),
        ('double_vision', 'Double vision'),
        ('visual_loss', 'Visual loss'),
        ('fever', 'Fever'),
        ('hearing_loss', 'Hearing loss'),
        ('confusion', 'Confusion'),
        ('drowsiness', 'Drowsiness'),
        ('behaviour_change', 'Behaviour change'),
        ('focal_weakness', 'Focal weakness'),
        ('seizures_lt_72 hrs', 'Seizures (<72 hrs)'),
        ('seizures_gt_72', 'Seizures (72 hrs - 1 mo)'),
        ('nausea', 'Nausea'),
        ('vomiting', 'Vomiting'),
        ('weight_loss', 'Weight Loss'),
        ('skin_lesions_cough', 'Skin Lesions Cough'),
        ('shortness_of_breath', 'Shortness of breath'),
    ],
}


for list_obj in list_data.keys():
    try:
        model = django_apps.get_app_config(
            list_obj.split('.')[0]).get_model(list_obj.split('.')[1])
        for tpl in list_data.get(list_obj):
            short_name, display_value = tpl
            try:
                obj = model.objects.get(short_name=short_name)
            except ObjectDoesNotExist:
                model.objects.create(short_name=short_name, name=display_value)
            else:
                obj.name = display_value
                obj.save()
    except Exception as e:
        print(e)