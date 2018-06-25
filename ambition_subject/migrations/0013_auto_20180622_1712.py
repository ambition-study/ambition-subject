# Generated by Django 2.0.4 on 2018-06-22 15:12

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ambition_subject', '0012_auto_20180622_1543'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalmedicalexpenses',
            name='someone_spent_last_4wks',
            field=models.DecimalField(decimal_places=2, help_text='On W10 record data for the ten weeks since recruitment.', max_digits=15, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Over the last 4/10 weeks, how much has someone else spent on activities relating to your health?'),
        ),
        migrations.AlterField(
            model_name='historicalmedicalexpenses',
            name='subject_spent_last_4wks',
            field=models.DecimalField(decimal_places=2, help_text='On W10 record data for the ten weeks since recruitment.', max_digits=15, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Over the last 4/10 weeks, how much have you spent on activities relating to your health?'),
        ),
        migrations.AlterField(
            model_name='historicalmedicalexpenses',
            name='total_spent_last_4wks',
            field=models.DecimalField(decimal_places=2, help_text='On W10 record data for the ten weeks since recruitment.', max_digits=16, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='How much in total has been spent on your healthcare in the last 4/10 weeks?'),
        ),
        migrations.AlterField(
            model_name='medicalexpenses',
            name='someone_spent_last_4wks',
            field=models.DecimalField(decimal_places=2, help_text='On W10 record data for the ten weeks since recruitment.', max_digits=15, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Over the last 4/10 weeks, how much has someone else spent on activities relating to your health?'),
        ),
        migrations.AlterField(
            model_name='medicalexpenses',
            name='subject_spent_last_4wks',
            field=models.DecimalField(decimal_places=2, help_text='On W10 record data for the ten weeks since recruitment.', max_digits=15, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Over the last 4/10 weeks, how much have you spent on activities relating to your health?'),
        ),
        migrations.AlterField(
            model_name='medicalexpenses',
            name='total_spent_last_4wks',
            field=models.DecimalField(decimal_places=2, help_text='On W10 record data for the ten weeks since recruitment.', max_digits=16, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='How much in total has been spent on your healthcare in the last 4/10 weeks?'),
        ),
    ]
