# Generated by Django 2.0.1 on 2018-01-06 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ambition_subject', '0005_auto_20180107_0037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bloodresult',
            name='alt_abnormal',
            field=models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=25, null=True, verbose_name='abnormal'),
        ),
        migrations.AlterField(
            model_name='bloodresult',
            name='alt_reportable',
            field=models.CharField(blank=True, choices=[('N/A', 'Not applicable'), ('No', 'No'), ('3', 'Grade 3'), ('4', 'Grade 4'), ('Already reported', 'Already reported')], max_length=25, null=True, verbose_name='reportable'),
        ),
        migrations.AlterField(
            model_name='bloodresult',
            name='cd4_abnormal',
            field=models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=25, null=True, verbose_name='abnormal'),
        ),
        migrations.AlterField(
            model_name='bloodresult',
            name='cd4_reportable',
            field=models.CharField(blank=True, choices=[('N/A', 'Not applicable'), ('No', 'No'), ('3', 'Grade 3'), ('4', 'Grade 4'), ('Already reported', 'Already reported')], max_length=25, null=True, verbose_name='reportable'),
        ),
        migrations.AlterField(
            model_name='bloodresult',
            name='creatinine_abnormal',
            field=models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=25, null=True, verbose_name='abnormal'),
        ),
        migrations.AlterField(
            model_name='bloodresult',
            name='creatinine_reportable',
            field=models.CharField(blank=True, choices=[('N/A', 'Not applicable'), ('No', 'No'), ('3', 'Grade 3'), ('4', 'Grade 4'), ('Already reported', 'Already reported')], max_length=25, null=True, verbose_name='reportable'),
        ),
        migrations.AlterField(
            model_name='bloodresult',
            name='creatinine_units',
            field=models.CharField(blank=True, choices=[('mg/dL', 'mg/dL'), ('umol/L', 'μmol/L')], max_length=25, null=True, verbose_name='units'),
        ),
        migrations.AlterField(
            model_name='bloodresult',
            name='haemoglobin',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=6, null=True),
        ),
        migrations.AlterField(
            model_name='bloodresult',
            name='haemoglobin_abnormal',
            field=models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=25, null=True, verbose_name='abnormal'),
        ),
        migrations.AlterField(
            model_name='bloodresult',
            name='haemoglobin_reportable',
            field=models.CharField(blank=True, choices=[('N/A', 'Not applicable'), ('No', 'No'), ('3', 'Grade 3'), ('4', 'Grade 4'), ('Already reported', 'Already reported')], max_length=25, null=True, verbose_name='reportable'),
        ),
        migrations.AlterField(
            model_name='bloodresult',
            name='magnesium_abnormal',
            field=models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=25, null=True, verbose_name='abnormal'),
        ),
        migrations.AlterField(
            model_name='bloodresult',
            name='magnesium_reportable',
            field=models.CharField(blank=True, choices=[('N/A', 'Not applicable'), ('No', 'No'), ('3', 'Grade 3'), ('4', 'Grade 4'), ('Already reported', 'Already reported')], max_length=25, null=True, verbose_name='reportable'),
        ),
        migrations.AlterField(
            model_name='bloodresult',
            name='magnesium_units',
            field=models.CharField(blank=True, choices=[('mg/dL', 'mg/dL'), ('mmol/L', 'mmol/L')], max_length=25, null=True, verbose_name='units'),
        ),
        migrations.AlterField(
            model_name='bloodresult',
            name='neutrophil',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True),
        ),
        migrations.AlterField(
            model_name='bloodresult',
            name='neutrophil_abnormal',
            field=models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=25, null=True, verbose_name='abnormal'),
        ),
        migrations.AlterField(
            model_name='bloodresult',
            name='neutrophil_reportable',
            field=models.CharField(blank=True, choices=[('N/A', 'Not applicable'), ('No', 'No'), ('3', 'Grade 3'), ('4', 'Grade 4'), ('Already reported', 'Already reported')], max_length=25, null=True, verbose_name='reportable'),
        ),
        migrations.AlterField(
            model_name='bloodresult',
            name='platelets_abnormal',
            field=models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=25, null=True, verbose_name='abnormal'),
        ),
        migrations.AlterField(
            model_name='bloodresult',
            name='platelets_reportable',
            field=models.CharField(blank=True, choices=[('N/A', 'Not applicable'), ('No', 'No'), ('3', 'Grade 3'), ('4', 'Grade 4'), ('Already reported', 'Already reported')], max_length=25, null=True, verbose_name='reportable'),
        ),
        migrations.AlterField(
            model_name='bloodresult',
            name='potassium_abnormal',
            field=models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=25, null=True, verbose_name='abnormal'),
        ),
        migrations.AlterField(
            model_name='bloodresult',
            name='potassium_reportable',
            field=models.CharField(blank=True, choices=[('N/A', 'Not applicable'), ('No', 'No'), ('3', 'Grade 3'), ('4', 'Grade 4'), ('Already reported', 'Already reported')], max_length=25, null=True, verbose_name='reportable'),
        ),
        migrations.AlterField(
            model_name='bloodresult',
            name='results_abnormal',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=25, verbose_name='Are any of the above results abnormal?'),
        ),
        migrations.AlterField(
            model_name='bloodresult',
            name='results_reportable',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('N/A', 'Not applicable')], help_text='If YES, this value will open Adverse Event Form.<br/><br/>Note: On Day 1 only abnormal bloods should not be reported as adverseevents.', max_length=25, verbose_name='If any results are abnormal, are results within grade III or above?'),
        ),
        migrations.AlterField(
            model_name='bloodresult',
            name='sodium_abnormal',
            field=models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=25, null=True, verbose_name='abnormal'),
        ),
        migrations.AlterField(
            model_name='bloodresult',
            name='sodium_reportable',
            field=models.CharField(blank=True, choices=[('N/A', 'Not applicable'), ('No', 'No'), ('3', 'Grade 3'), ('4', 'Grade 4'), ('Already reported', 'Already reported')], max_length=25, null=True, verbose_name='reportable'),
        ),
        migrations.AlterField(
            model_name='bloodresult',
            name='urea_abnormal',
            field=models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=25, null=True, verbose_name='abnormal'),
        ),
        migrations.AlterField(
            model_name='bloodresult',
            name='urea_reportable',
            field=models.CharField(blank=True, choices=[('N/A', 'Not applicable'), ('No', 'No'), ('3', 'Grade 3'), ('4', 'Grade 4'), ('Already reported', 'Already reported')], max_length=25, null=True, verbose_name='reportable'),
        ),
        migrations.AlterField(
            model_name='bloodresult',
            name='urea_units',
            field=models.CharField(blank=True, choices=[('mg/dL', 'mg/dL'), ('mmol/L', 'mmol/L')], max_length=25, null=True, verbose_name='units'),
        ),
        migrations.AlterField(
            model_name='bloodresult',
            name='vl_abnormal',
            field=models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=25, null=True, verbose_name='abnormal'),
        ),
        migrations.AlterField(
            model_name='bloodresult',
            name='vl_reportable',
            field=models.CharField(blank=True, choices=[('N/A', 'Not applicable'), ('No', 'No'), ('3', 'Grade 3'), ('4', 'Grade 4'), ('Already reported', 'Already reported')], max_length=25, null=True, verbose_name='reportable'),
        ),
        migrations.AlterField(
            model_name='bloodresult',
            name='wbc',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=6, null=True, verbose_name='WBC'),
        ),
        migrations.AlterField(
            model_name='bloodresult',
            name='wbc_abnormal',
            field=models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=25, null=True, verbose_name='abnormal'),
        ),
        migrations.AlterField(
            model_name='bloodresult',
            name='wbc_reportable',
            field=models.CharField(blank=True, choices=[('N/A', 'Not applicable'), ('No', 'No'), ('3', 'Grade 3'), ('4', 'Grade 4'), ('Already reported', 'Already reported')], max_length=25, null=True, verbose_name='reportable'),
        ),
        migrations.AlterField(
            model_name='historicalbloodresult',
            name='alt_abnormal',
            field=models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=25, null=True, verbose_name='abnormal'),
        ),
        migrations.AlterField(
            model_name='historicalbloodresult',
            name='alt_reportable',
            field=models.CharField(blank=True, choices=[('N/A', 'Not applicable'), ('No', 'No'), ('3', 'Grade 3'), ('4', 'Grade 4'), ('Already reported', 'Already reported')], max_length=25, null=True, verbose_name='reportable'),
        ),
        migrations.AlterField(
            model_name='historicalbloodresult',
            name='cd4_abnormal',
            field=models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=25, null=True, verbose_name='abnormal'),
        ),
        migrations.AlterField(
            model_name='historicalbloodresult',
            name='cd4_reportable',
            field=models.CharField(blank=True, choices=[('N/A', 'Not applicable'), ('No', 'No'), ('3', 'Grade 3'), ('4', 'Grade 4'), ('Already reported', 'Already reported')], max_length=25, null=True, verbose_name='reportable'),
        ),
        migrations.AlterField(
            model_name='historicalbloodresult',
            name='creatinine_abnormal',
            field=models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=25, null=True, verbose_name='abnormal'),
        ),
        migrations.AlterField(
            model_name='historicalbloodresult',
            name='creatinine_reportable',
            field=models.CharField(blank=True, choices=[('N/A', 'Not applicable'), ('No', 'No'), ('3', 'Grade 3'), ('4', 'Grade 4'), ('Already reported', 'Already reported')], max_length=25, null=True, verbose_name='reportable'),
        ),
        migrations.AlterField(
            model_name='historicalbloodresult',
            name='creatinine_units',
            field=models.CharField(blank=True, choices=[('mg/dL', 'mg/dL'), ('umol/L', 'μmol/L')], max_length=25, null=True, verbose_name='units'),
        ),
        migrations.AlterField(
            model_name='historicalbloodresult',
            name='haemoglobin',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=6, null=True),
        ),
        migrations.AlterField(
            model_name='historicalbloodresult',
            name='haemoglobin_abnormal',
            field=models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=25, null=True, verbose_name='abnormal'),
        ),
        migrations.AlterField(
            model_name='historicalbloodresult',
            name='haemoglobin_reportable',
            field=models.CharField(blank=True, choices=[('N/A', 'Not applicable'), ('No', 'No'), ('3', 'Grade 3'), ('4', 'Grade 4'), ('Already reported', 'Already reported')], max_length=25, null=True, verbose_name='reportable'),
        ),
        migrations.AlterField(
            model_name='historicalbloodresult',
            name='magnesium_abnormal',
            field=models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=25, null=True, verbose_name='abnormal'),
        ),
        migrations.AlterField(
            model_name='historicalbloodresult',
            name='magnesium_reportable',
            field=models.CharField(blank=True, choices=[('N/A', 'Not applicable'), ('No', 'No'), ('3', 'Grade 3'), ('4', 'Grade 4'), ('Already reported', 'Already reported')], max_length=25, null=True, verbose_name='reportable'),
        ),
        migrations.AlterField(
            model_name='historicalbloodresult',
            name='magnesium_units',
            field=models.CharField(blank=True, choices=[('mg/dL', 'mg/dL'), ('mmol/L', 'mmol/L')], max_length=25, null=True, verbose_name='units'),
        ),
        migrations.AlterField(
            model_name='historicalbloodresult',
            name='neutrophil',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True),
        ),
        migrations.AlterField(
            model_name='historicalbloodresult',
            name='neutrophil_abnormal',
            field=models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=25, null=True, verbose_name='abnormal'),
        ),
        migrations.AlterField(
            model_name='historicalbloodresult',
            name='neutrophil_reportable',
            field=models.CharField(blank=True, choices=[('N/A', 'Not applicable'), ('No', 'No'), ('3', 'Grade 3'), ('4', 'Grade 4'), ('Already reported', 'Already reported')], max_length=25, null=True, verbose_name='reportable'),
        ),
        migrations.AlterField(
            model_name='historicalbloodresult',
            name='platelets_abnormal',
            field=models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=25, null=True, verbose_name='abnormal'),
        ),
        migrations.AlterField(
            model_name='historicalbloodresult',
            name='platelets_reportable',
            field=models.CharField(blank=True, choices=[('N/A', 'Not applicable'), ('No', 'No'), ('3', 'Grade 3'), ('4', 'Grade 4'), ('Already reported', 'Already reported')], max_length=25, null=True, verbose_name='reportable'),
        ),
        migrations.AlterField(
            model_name='historicalbloodresult',
            name='potassium_abnormal',
            field=models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=25, null=True, verbose_name='abnormal'),
        ),
        migrations.AlterField(
            model_name='historicalbloodresult',
            name='potassium_reportable',
            field=models.CharField(blank=True, choices=[('N/A', 'Not applicable'), ('No', 'No'), ('3', 'Grade 3'), ('4', 'Grade 4'), ('Already reported', 'Already reported')], max_length=25, null=True, verbose_name='reportable'),
        ),
        migrations.AlterField(
            model_name='historicalbloodresult',
            name='results_abnormal',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=25, verbose_name='Are any of the above results abnormal?'),
        ),
        migrations.AlterField(
            model_name='historicalbloodresult',
            name='results_reportable',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('N/A', 'Not applicable')], help_text='If YES, this value will open Adverse Event Form.<br/><br/>Note: On Day 1 only abnormal bloods should not be reported as adverseevents.', max_length=25, verbose_name='If any results are abnormal, are results within grade III or above?'),
        ),
        migrations.AlterField(
            model_name='historicalbloodresult',
            name='sodium_abnormal',
            field=models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=25, null=True, verbose_name='abnormal'),
        ),
        migrations.AlterField(
            model_name='historicalbloodresult',
            name='sodium_reportable',
            field=models.CharField(blank=True, choices=[('N/A', 'Not applicable'), ('No', 'No'), ('3', 'Grade 3'), ('4', 'Grade 4'), ('Already reported', 'Already reported')], max_length=25, null=True, verbose_name='reportable'),
        ),
        migrations.AlterField(
            model_name='historicalbloodresult',
            name='urea_abnormal',
            field=models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=25, null=True, verbose_name='abnormal'),
        ),
        migrations.AlterField(
            model_name='historicalbloodresult',
            name='urea_reportable',
            field=models.CharField(blank=True, choices=[('N/A', 'Not applicable'), ('No', 'No'), ('3', 'Grade 3'), ('4', 'Grade 4'), ('Already reported', 'Already reported')], max_length=25, null=True, verbose_name='reportable'),
        ),
        migrations.AlterField(
            model_name='historicalbloodresult',
            name='urea_units',
            field=models.CharField(blank=True, choices=[('mg/dL', 'mg/dL'), ('mmol/L', 'mmol/L')], max_length=25, null=True, verbose_name='units'),
        ),
        migrations.AlterField(
            model_name='historicalbloodresult',
            name='vl_abnormal',
            field=models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=25, null=True, verbose_name='abnormal'),
        ),
        migrations.AlterField(
            model_name='historicalbloodresult',
            name='vl_reportable',
            field=models.CharField(blank=True, choices=[('N/A', 'Not applicable'), ('No', 'No'), ('3', 'Grade 3'), ('4', 'Grade 4'), ('Already reported', 'Already reported')], max_length=25, null=True, verbose_name='reportable'),
        ),
        migrations.AlterField(
            model_name='historicalbloodresult',
            name='wbc',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=6, null=True, verbose_name='WBC'),
        ),
        migrations.AlterField(
            model_name='historicalbloodresult',
            name='wbc_abnormal',
            field=models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=25, null=True, verbose_name='abnormal'),
        ),
        migrations.AlterField(
            model_name='historicalbloodresult',
            name='wbc_reportable',
            field=models.CharField(blank=True, choices=[('N/A', 'Not applicable'), ('No', 'No'), ('3', 'Grade 3'), ('4', 'Grade 4'), ('Already reported', 'Already reported')], max_length=25, null=True, verbose_name='reportable'),
        ),
    ]