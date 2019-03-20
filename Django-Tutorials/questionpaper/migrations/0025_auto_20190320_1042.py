# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2019-03-20 05:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questionpaper', '0024_auto_20190320_1028'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listeninganswer',
            old_name='mcq_idb',
            new_name='fillup_idb3',
        ),
        migrations.AddField(
            model_name='listeninganswer',
            name='fillup_idb4',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='listeninganswer',
            name='fillupb3',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='listeninganswer',
            name='fillupb4',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='listeninganswer',
            name='mcq_idb0',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='listeninganswer',
            name='mcq_idb1',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='listeninganswer',
            name='mcq_idb2',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='listeninganswer',
            name='mcq_idb3',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='listeninganswer',
            name='mcqb1',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='listeninganswer',
            name='mcqb2',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='listeninganswer',
            name='mcqb3',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
