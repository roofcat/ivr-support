# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-19 20:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calls', '0004_auto_20160519_1520'),
    ]

    operations = [
        migrations.AlterField(
            model_name='call',
            name='dialIntentCalled1',
            field=models.BigIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='call',
            name='dialIntentCaller1',
            field=models.BigIntegerField(null=True),
        ),
    ]