# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2019-03-20 09:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questionpaper', '0027_auto_20190320_1238'),
    ]

    operations = [
        migrations.AddField(
            model_name='readinganswer',
            name='fillup_idb3',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='readinganswer',
            name='fillupb3',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='readinganswer',
            name='mcq_idc1',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='readinganswer',
            name='mcqc1',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
