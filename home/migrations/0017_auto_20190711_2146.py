# Generated by Django 2.2.1 on 2019-07-11 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_auto_20190711_1834'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='type',
            field=models.CharField(default='user', max_length=10),
        ),
        migrations.AddField(
            model_name='workplace',
            name='desc',
            field=models.CharField(default='', max_length=500),
        ),
    ]