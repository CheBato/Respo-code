# Generated by Django 2.2.1 on 2019-08-10 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20190810_1559'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='image',
            field=models.CharField(default='user_icon.png', max_length=100),
        ),
    ]
