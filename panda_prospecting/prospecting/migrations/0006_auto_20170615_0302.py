# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-15 03:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prospecting', '0005_auto_20170615_0259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prospect',
            name='full_name',
            field=models.CharField(max_length=200),
        ),
    ]
