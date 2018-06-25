# Generated by Django 2.0.5 on 2018-06-04 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ambition_subject', '0010_auto_20180512_1248'),
    ]

    operations = [
        migrations.AddField(
            model_name='followup',
            name='antibiotics',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('N/A', 'Not applicable')], max_length=5, null=True, verbose_name='Since week two, were any of the following antibiotics given?'),
        ),
        migrations.AddField(
            model_name='followup',
            name='blood_transfusions',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=5, null=True, verbose_name='Has the patient had any blood transfusions since week two? '),
        ),
        migrations.AddField(
            model_name='followup',
            name='blood_transfusions_units',
            field=models.DecimalField(decimal_places=3, max_digits=4, null=True, verbose_name='If YES, no. of units?    '),
        ),
        migrations.AddField(
            model_name='followup',
            name='days_hospitalized',
            field=models.DecimalField(decimal_places=3, max_digits=4, null=True, verbose_name='Over the ten weeks spent in the study how many days did the patient spend in hospital?'),
        ),
        migrations.AddField(
            model_name='historicalfollowup',
            name='antibiotics',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('N/A', 'Not applicable')], max_length=5, null=True, verbose_name='Since week two, were any of the following antibiotics given?'),
        ),
        migrations.AddField(
            model_name='historicalfollowup',
            name='blood_transfusions',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=5, null=True, verbose_name='Has the patient had any blood transfusions since week two? '),
        ),
        migrations.AddField(
            model_name='historicalfollowup',
            name='blood_transfusions_units',
            field=models.DecimalField(decimal_places=3, max_digits=4, null=True, verbose_name='If YES, no. of units?    '),
        ),
        migrations.AddField(
            model_name='historicalfollowup',
            name='days_hospitalized',
            field=models.DecimalField(decimal_places=3, max_digits=4, null=True, verbose_name='Over the ten weeks spent in the study how many days did the patient spend in hospital?'),
        ),
    ]
