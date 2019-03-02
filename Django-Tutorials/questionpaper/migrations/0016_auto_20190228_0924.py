# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2019-02-28 03:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questionpaper', '0015_listeninganswer'),
    ]

    operations = [
        migrations.AddField(
            model_name='listeninganswer',
            name='mat0',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='listeninganswer',
            name='mat1',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='listeninganswer',
            name='mat2',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='listeninganswer',
            name='mat3',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='listeninganswer',
            name='mat4',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='listeninganswer',
            name='mat5',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='listeninganswer',
            name='mat_id0',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='listeninganswer',
            name='mat_id1',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='listeninganswer',
            name='mat_id2',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='listeninganswer',
            name='mat_id3',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='listeninganswer',
            name='mat_id4',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='listeninganswer',
            name='mat_id5',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='readinganswer',
            name='mat0',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='readinganswer',
            name='mat1',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='readinganswer',
            name='mat2',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='readinganswer',
            name='mat3',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='readinganswer',
            name='mat4',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='readinganswer',
            name='mat5',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='readinganswer',
            name='mat_id',
            field=models.IntegerField(null=True),
        ),
    ]