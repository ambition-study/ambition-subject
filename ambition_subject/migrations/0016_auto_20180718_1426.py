# Generated by Django 2.0.4 on 2018-07-18 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ambition_subject', '0015_auto_20180711_1626'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalpkpdcrf',
            name='blood_sample_missed',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('N/A', 'Not applicable')], default='N/A', max_length=11, null=True, verbose_name='Were any blood samples missed?'),
        ),
        migrations.AlterField(
            model_name='historicalpkpdcrf',
            name='fluconazole_dose_given',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=11, null=True, verbose_name='Was the Fluconazole dose given?'),
        ),
        migrations.AlterField(
            model_name='historicalpkpdcrf',
            name='flucytosine_dose_four_given',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('N/A', 'Not applicable')], default='N/A', max_length=11, null=True, verbose_name='Flucytosine <u>DOSE&nbsp;4</u> given? '),
        ),
        migrations.AlterField(
            model_name='historicalpkpdcrf',
            name='flucytosine_dose_one_given',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('N/A', 'Not applicable')], default='N/A', max_length=11, null=True, verbose_name='Flucytosine <u>DOSE&nbsp;1</u> given? '),
        ),
        migrations.AlterField(
            model_name='historicalpkpdcrf',
            name='flucytosine_dose_three_given',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('N/A', 'Not applicable')], default='N/A', max_length=11, null=True, verbose_name='Flucytosine <u>DOSE&nbsp;3</u> given? '),
        ),
        migrations.AlterField(
            model_name='historicalpkpdcrf',
            name='flucytosine_dose_two_given',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('N/A', 'Not applicable')], default='N/A', max_length=11, null=True, verbose_name='Flucytosine <u>DOSE&nbsp;2</u> given? '),
        ),
        migrations.AlterField(
            model_name='historicalpkpdcrf',
            name='full_ambisome_dose_given',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('N/A', 'Not applicable')], default='N/A', max_length=11, null=True, verbose_name='Was the entire Ambisome dose given?'),
        ),
        migrations.AlterField(
            model_name='pkpdcrf',
            name='blood_sample_missed',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('N/A', 'Not applicable')], default='N/A', max_length=11, null=True, verbose_name='Were any blood samples missed?'),
        ),
        migrations.AlterField(
            model_name='pkpdcrf',
            name='fluconazole_dose_given',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=11, null=True, verbose_name='Was the Fluconazole dose given?'),
        ),
        migrations.AlterField(
            model_name='pkpdcrf',
            name='flucytosine_dose_four_given',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('N/A', 'Not applicable')], default='N/A', max_length=11, null=True, verbose_name='Flucytosine <u>DOSE&nbsp;4</u> given? '),
        ),
        migrations.AlterField(
            model_name='pkpdcrf',
            name='flucytosine_dose_one_given',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('N/A', 'Not applicable')], default='N/A', max_length=11, null=True, verbose_name='Flucytosine <u>DOSE&nbsp;1</u> given? '),
        ),
        migrations.AlterField(
            model_name='pkpdcrf',
            name='flucytosine_dose_three_given',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('N/A', 'Not applicable')], default='N/A', max_length=11, null=True, verbose_name='Flucytosine <u>DOSE&nbsp;3</u> given? '),
        ),
        migrations.AlterField(
            model_name='pkpdcrf',
            name='flucytosine_dose_two_given',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('N/A', 'Not applicable')], default='N/A', max_length=11, null=True, verbose_name='Flucytosine <u>DOSE&nbsp;2</u> given? '),
        ),
        migrations.AlterField(
            model_name='pkpdcrf',
            name='full_ambisome_dose_given',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('N/A', 'Not applicable')], default='N/A', max_length=11, null=True, verbose_name='Was the entire Ambisome dose given?'),
        ),
    ]
