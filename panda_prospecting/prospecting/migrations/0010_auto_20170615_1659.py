# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-15 16:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prospecting', '0009_auto_20170615_0428'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='account',
            options={'verbose_name_plural': 'accounts'},
        ),
        migrations.AlterModelOptions(
            name='prospect',
            options={'verbose_name_plural': 'prospects'},
        ),
        migrations.AddField(
            model_name='prospect',
            name='prospect_notes',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
