# Generated by Django 3.2.4 on 2021-07-01 14:30

import django.core.validators
from django.db import migrations, models
import lib.fields
import re


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0048_delete_duplicate_enrollments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='url',
            field=models.CharField(help_text='COURSE_URL_IDENTIFIER_HELPTEXT', max_length=255, unique=True, validators=[django.core.validators.RegexValidator(message='URL_KEY_MAY_CONSIST_OF', regex=re.compile('^\\w[\\w\\-\\.]*$'))]),
        ),
        migrations.AlterField(
            model_name='courseinstance',
            name='content_numbering',
            field=models.IntegerField(choices=[(0, 'NUMBERING_NONE'), (1, 'NUMBERING_ARABIC'), (2, 'NUMBERING_ROMAN'), (3, 'NUMBERING_HIDDEN_ARABIC')], default=1),
        ),
        migrations.AlterField(
            model_name='courseinstance',
            name='enrollment_audience',
            field=models.IntegerField(choices=[(1, 'INTERNAL_USERS'), (2, 'EXTERNAL_USERS'), (3, 'ALL_USERS')], default=1),
        ),
        migrations.AlterField(
            model_name='courseinstance',
            name='head_urls',
            field=models.TextField(blank=True, help_text='COURSE_INSTANCE_EXTERNAL_CSS_AND_JS_FOR_ALL_PAGES_HELPTEXT'),
        ),
        migrations.AlterField(
            model_name='courseinstance',
            name='index_mode',
            field=models.IntegerField(choices=[(0, 'USER_RESULTS'), (1, 'TABLE_OF_CONTENTS'), (2, 'LAST_VISITED_LINK'), (10, 'EXPERIMENTAL_SETUP')], default=0, help_text='COURSE_INSTANCE_INDEX_CONTENT_SELECTION_HELPTEXT'),
        ),
        migrations.AlterField(
            model_name='courseinstance',
            name='module_numbering',
            field=models.IntegerField(choices=[(0, 'NUMBERING_NONE'), (1, 'NUMBERING_ARABIC'), (2, 'NUMBERING_ROMAN'), (3, 'NUMBERING_HIDDEN_ARABIC')], default=1),
        ),
        migrations.AlterField(
            model_name='courseinstance',
            name='technical_error_emails',
            field=models.CharField(blank=True, help_text='COURSE_INSTANCE_EXERCISE_ERROR_EMAIL_RECIPIENT_OVERRIDE_HELPTEXT', max_length=255),
        ),
        migrations.AlterField(
            model_name='courseinstance',
            name='url',
            field=models.CharField(help_text='COURSE_INSTANCE_URL_IDENTIFIER_HELPTEXT', max_length=255, validators=[django.core.validators.RegexValidator(message='URL_KEY_MAY_CONSIST_OF', regex=re.compile('^\\w[\\w\\-\\.]*$'))]),
        ),
        migrations.AlterField(
            model_name='courseinstance',
            name='view_content_to',
            field=models.IntegerField(choices=[(1, 'ENROLLED_STUDENTS'), (2, 'ENROLLMENT_AUDIENCE'), (3, 'ALL_REGISTERED_USERS'), (4, 'PUBLIC')], default=1),
        ),
        migrations.AlterField(
            model_name='coursemodule',
            name='late_submission_penalty',
            field=lib.fields.PercentField(default=0.5, help_text='MODULE_LATE_SUBMISSION_PENALTY_HELPTEXT'),
        ),
        migrations.AlterField(
            model_name='coursemodule',
            name='reading_opening_time',
            field=models.DateTimeField(blank=True, help_text='MODULE_READING_OPENING_TIME_HELPTEXT', null=True, verbose_name='MODULE_READING_OPENING_TIME_VERBOSE'),
        ),
        migrations.AlterField(
            model_name='coursemodule',
            name='status',
            field=models.CharField(choices=[('hidden', 'STATUS_HIDDEN'), ('maintenance', 'STATUS_MAINTENANCE'), ('ready', 'STATUS_READY'), ('unlisted', 'STATUS_UNLISTED')], default='ready', max_length=32),
        ),
        migrations.AlterField(
            model_name='coursemodule',
            name='url',
            field=models.CharField(help_text='MODULE_URL_IDENTIFIER_HELPTEXT', max_length=255, validators=[django.core.validators.RegexValidator(message='URL_KEY_MAY_CONSIST_OF', regex=re.compile('^\\w[\\w\\-\\.]*$'))]),
        ),
        migrations.AlterField(
            model_name='learningobjectcategory',
            name='accept_unofficial_submits',
            field=models.BooleanField(default=False, help_text='LEARNING_OBJECT_CATEGORY_ACCEPT_UNOFFICIAL_SUBMISSIONS_HELPTEXT'),
        ),
        migrations.AlterField(
            model_name='learningobjectcategory',
            name='confirm_the_level',
            field=models.BooleanField(default=False, help_text='LEARNING_OBJECT_CATEGORY_LEVEL_CONFIRMATION_EXERCISE_HELPTEXT'),
        ),
        migrations.AlterField(
            model_name='learningobjectcategory',
            name='status',
            field=models.CharField(choices=[('hidden', 'STATUS_HIDDEN'), ('nototal', 'STATUS_NO_TOTAL_POINTS'), ('ready', 'STATUS_READY')], default='ready', max_length=32),
        ),
    ]