# Generated by Django 2.2.1 on 2019-07-10 08:08

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_education_desc'),
    ]

    operations = [
        migrations.RenameField(
            model_name='competence',
            old_name='name',
            new_name='slo_name',
        ),
        migrations.RemoveField(
            model_name='participation',
            name='time',
        ),
        migrations.AddField(
            model_name='competence',
            name='eng_name',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='education',
            name='date_from',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='education',
            name='date_to',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='participation',
            name='participated',
            field=models.BooleanField(default=False),
        ),
    ]
