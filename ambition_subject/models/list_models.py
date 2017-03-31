from edc_base.model_mixins import ListModelMixin, BaseUuidModel


class AEClassification(ListModelMixin, BaseUuidModel):

    class Meta(ListModelMixin.Meta):
        app_label = 'ambition_subject'


class Antibiotics(ListModelMixin, BaseUuidModel):

    class Meta(ListModelMixin.Meta):
        app_label = 'ambition_subject'


class MeningitisSymptoms(ListModelMixin, BaseUuidModel):

    class Meta(ListModelMixin.Meta):
        app_label = 'ambition_subject'


class Neurological(ListModelMixin, BaseUuidModel):

    class Meta(ListModelMixin.Meta):
        app_label = 'ambition_subject'


class MissedVisitReasons(ListModelMixin, BaseUuidModel):

    class Meta(ListModelMixin.Meta):
        app_label = 'ambition_subject'


class SignificantNewDiagnoses(ListModelMixin, BaseUuidModel):

    class Meta(ListModelMixin.Meta):
        app_label = 'ambition_subject'


class Symptoms(ListModelMixin, BaseUuidModel):

    class Meta(ListModelMixin.Meta):
        app_label = 'ambition_subject'


class Otherdruglist(ListModelMixin, BaseUuidModel):

    class Meta(ListModelMixin.Meta):
        app_label = 'ambition_subject'
