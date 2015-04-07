# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20150330_1919'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='recipes',
            field=models.ManyToManyField(to='blog.Recipe'),
        ),
        migrations.AddField(
            model_name='recipe',
            name='cook_time',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recipe',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2015, 4, 7, 15, 28, 21, 163544)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recipe',
            name='instructions',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recipe',
            name='prep_time',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='diet',
            name='name',
            field=models.CharField(default='NO', max_length=2, choices=[('DF', 'Dairy Free'), ('GF', 'Gluten Free'), ('RW', 'Raw'), ('VG', 'Vegan'), ('VT', 'Vegetarian'), ('NO', 'None')]),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='season',
            field=models.CharField(default='ANY', max_length=3, choices=[('SPR', 'Spring'), ('SUM', 'Summer'), ('FAL', 'Fall'), ('WIN', 'Winter'), ('ANY', 'Any')]),
        ),
    ]
