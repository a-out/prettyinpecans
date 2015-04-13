# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20150413_0102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diet',
            name='name',
            field=models.CharField(default='NO', max_length=2, unique=True, choices=[('DF', 'Dairy Free'), ('GF', 'Gluten Free'), ('RW', 'Raw'), ('VG', 'Vegan'), ('VT', 'Vegetarian'), ('NO', 'None')]),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='mealtype',
            name='name',
            field=models.CharField(max_length=32, unique=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='recipes',
            field=models.ManyToManyField(blank=True, related_name='posts', to='blog.Recipe'),
        ),
    ]
