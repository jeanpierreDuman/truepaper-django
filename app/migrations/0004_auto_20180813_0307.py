# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-08-13 01:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20180813_0250'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='oldMachineBadPoint',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='article',
            name='oldMachineGoodPoint',
            field=models.IntegerField(default=0),
        ),
    ]
