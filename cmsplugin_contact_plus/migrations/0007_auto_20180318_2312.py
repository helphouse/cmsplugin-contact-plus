# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-18 22:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmsplugin_contact_plus', '0006_auto_20180313_1342'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactplus',
            name='email_template',
            field=models.CharField(choices=[('cmsplugin_contact_plus/email.txt', 'Default')], default='cmsplugin_contact_plus/email.txt', max_length=255, verbose_name='Email template'),
        ),
        migrations.AlterField(
            model_name='contactplus',
            name='template',
            field=models.CharField(choices=[('cmsplugin_contact_plus/contact.html', 'contact.html')], default='cmsplugin_contact_plus/contact.html', editable=False, max_length=255),
        ),
        migrations.AlterField(
            model_name='contactrecord',
            name='date_processed',
            field=models.DateTimeField(blank=True, help_text='Date the Record was processed.', null=True),
        ),
    ]
