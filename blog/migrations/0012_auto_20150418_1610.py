# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_post_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diet',
            name='name',
            field=models.CharField(unique=True, max_length=32, default='None'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='diets',
            field=models.ManyToManyField(to='blog.Diet', related_name='recipes'),
        ),
    ]
