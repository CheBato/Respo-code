# Generated by Django 2.2.1 on 2019-08-08 13:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_hr_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hr_user',
            name='id_workplace',
        ),
    ]