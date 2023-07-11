# Generated by Django 3.2.18 on 2023-06-09 13:39

from django.db import migrations, models
import django.db.models.deletion
import lib.fields


class Migration(migrations.Migration):

    dependencies = [
        ('external_services', '0017_lti1p3service'),
        ('exercise', '0046_pendingsubmission'),
    ]

    operations = [
        migrations.CreateModel(
            name='LTI1p3Exercise',
            fields=[
                ('baseexercise_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='exercise.baseexercise')),
                ('custom', models.TextField(blank=True, help_text='LTI_CUSTOM_PARAMETERS_HELPTEXT', verbose_name='LABEL_LTI_CUSTOM_PARAMETERS')),
                ('open_in_iframe', models.BooleanField(default=False, help_text='LTI_EXERCISE_OPEN_IN_IFRAME_HELPTEXT', verbose_name='LABEL_OPEN_IN_IFRAME')),
                ('lti_service', lib.fields.DefaultForeignKey(on_delete=django.db.models.deletion.CASCADE, to='external_services.lti1p3service', verbose_name='LABEL_LTI_SERVICE')),
            ],
            options={
                'verbose_name': 'MODEL_NAME_LTI1P3_EXERCISE',
                'verbose_name_plural': 'MODEL_NAME_LTI1P3_EXERCISE_PLURAL',
            },
            bases=('exercise.baseexercise',),
        ),
    ]