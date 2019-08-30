# Generated by Django 2.2.1 on 2019-08-07 12:38

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='myuser',
            fields=[
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('id_user', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.CharField(max_length=100, unique=True)),
                ('password', models.CharField(max_length=500)),
                ('is_employee', models.BooleanField(default=False)),
                ('is_HR', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='competence',
            fields=[
                ('id_competence', models.AutoField(primary_key=True, serialize=False)),
                ('hoegen_id', models.IntegerField(default=0, unique=True)),
                ('slo_name', models.CharField(max_length=100)),
                ('eng_name', models.CharField(blank=True, max_length=100)),
                ('desc', models.CharField(blank=True, default='', max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='competence_type',
            fields=[
                ('id_competence_type', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='education',
            fields=[
                ('id_education', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('desc', models.CharField(blank=True, max_length=500)),
                ('date_from', models.DateField(default=django.utils.timezone.now)),
                ('date_to', models.DateField(default=django.utils.timezone.now)),
                ('id_competence', models.ManyToManyField(to='home.competence')),
            ],
        ),
        migrations.CreateModel(
            name='employee',
            fields=[
                ('id_employee', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(default='', max_length=100)),
                ('last_name', models.CharField(default='', max_length=100)),
                ('phone', models.CharField(default='', max_length=100)),
                ('city', models.CharField(default='', max_length=100)),
                ('country', models.CharField(default='', max_length=100)),
                ('email', models.CharField(default='', max_length=100, unique=True)),
                ('username', models.CharField(default='', max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='workplace',
            fields=[
                ('id_workplace', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('desc', models.CharField(default='', max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='participation',
            fields=[
                ('id_participation', models.AutoField(primary_key=True, serialize=False)),
                ('participated', models.BooleanField(default=False)),
                ('status', models.CharField(default='', max_length=100)),
                ('id_education', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.education')),
                ('id_employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.employee')),
            ],
        ),
        migrations.CreateModel(
            name='notifications',
            fields=[
                ('id_notification', models.AutoField(primary_key=True, serialize=False)),
                ('seen', models.BooleanField(default=False)),
                ('for_employee', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='home.employee')),
                ('id_education', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.education')),
            ],
        ),
        migrations.CreateModel(
            name='employee_history',
            fields=[
                ('id_employee_history', models.AutoField(primary_key=True, serialize=False)),
                ('level', models.IntegerField()),
                ('dateOfChange', models.DateField(default=django.utils.timezone.now)),
                ('id_competence', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.competence')),
                ('id_employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.employee')),
            ],
        ),
        migrations.CreateModel(
            name='employee_competence',
            fields=[
                ('id_employee_competence', models.AutoField(primary_key=True, serialize=False)),
                ('level', models.IntegerField()),
                ('id_competence', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.competence')),
                ('id_competence_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.competence_type')),
                ('id_employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.employee')),
            ],
        ),
        migrations.AddField(
            model_name='employee',
            name='id_workplace',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='home.workplace'),
        ),
        migrations.AddField(
            model_name='employee',
            name='user',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='competence_relevance',
            fields=[
                ('id_competence_relevance', models.AutoField(primary_key=True, serialize=False)),
                ('competence_weight', models.IntegerField()),
                ('minimum_required', models.IntegerField(default=0)),
                ('id_competence', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.competence')),
                ('id_workplace', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.workplace')),
            ],
        ),
        migrations.AddField(
            model_name='competence',
            name='id_competence_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.competence_type'),
        ),
    ]
