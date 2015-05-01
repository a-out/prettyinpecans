# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_auto_20150418_1610'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diet',
            name='name',
            field=models.CharField(max_length=32, unique=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='diets',
            field=models.ManyToManyField(blank=True, to='blog.Diet', related_name='recipes'),
        ),
    ]
