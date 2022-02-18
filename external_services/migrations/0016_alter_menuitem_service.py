# Generated by Django 3.2.4 on 2022-02-11 13:40

from django.db import migrations
import django.db.models.deletion
import lib.fields


class Migration(migrations.Migration):

    dependencies = [
        ('external_services', '0015_auto_20210812_1536'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitem',
            name='service',
            field=lib.fields.DefaultForeignKey(blank=True, help_text='MENU_ITEM_SERVICE_HELPTEXT', null=True, on_delete=django.db.models.deletion.CASCADE, to='external_services.linkservice', verbose_name='LABEL_SERVICE'),
        ),
    ]