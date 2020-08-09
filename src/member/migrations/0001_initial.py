# Generated by Django 3.0.5 on 2020-08-08 13:37

import backend.validators
from django.conf import settings
import django.contrib.auth.models
import django.contrib.postgres.fields.citext
from django.contrib.postgres.operations import CITextExtension
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import member.models
import secrets


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        CITextExtension(),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('username', django.contrib.postgres.fields.citext.CICharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 36 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=36, unique=True, validators=[backend.validators.NameValidator()], verbose_name='username')),
                ('email', models.EmailField(blank=True, max_length=254, unique=True, verbose_name='email address')),
                ('totp_secret', models.CharField(max_length=16, null=True)),
                ('totp_status', models.IntegerField(choices=[(member.models.TOTPStatus['DISABLED'], 0), (member.models.TOTPStatus['VERIFYING'], 1), (member.models.TOTPStatus['ENABLED'], 2)], default=member.models.TOTPStatus['DISABLED'])),
                ('is_visible', models.BooleanField(default=False)),
                ('bio', models.TextField(blank=True, max_length=400)),
                ('discord', models.CharField(blank=True, max_length=36)),
                ('discordid', models.CharField(blank=True, max_length=18)),
                ('twitter', models.CharField(blank=True, max_length=36)),
                ('reddit', models.CharField(blank=True, max_length=36)),
                ('email_verified', models.BooleanField(default=False)),
                ('email_token', models.CharField(default=secrets.token_hex, max_length=64)),
                ('password_reset_token', models.CharField(default=secrets.token_hex, max_length=64)),
                ('points', models.IntegerField(default=0)),
                ('leaderboard_points', models.IntegerField(default=0)),
                ('last_score', models.DateTimeField(default=django.utils.timezone.now)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
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
            name='UserIP',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=255)),
                ('seen', models.IntegerField(default=1)),
                ('last_seen', models.DateTimeField(default=django.utils.timezone.now)),
                ('user_agent', models.CharField(max_length=255)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
