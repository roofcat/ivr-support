# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-19 19:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calls', '0003_auto_20160519_1308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='call',
            name='lastState',
            field=models.CharField(max_length=150, null=True),
        ),
    ]
