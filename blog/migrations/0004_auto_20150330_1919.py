# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_diet_ingredient_mealtype_recipe'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='header_image',
            field=models.ForeignKey(default=None, related_name='title_post', to='blog.Image'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='diet',
            name='name',
            field=models.CharField(choices=[('DF', 'Dairy Free'), ('GF', 'Gluten Free'), ('RW', 'Raw'), ('VG', 'Vegan'), ('VT', 'Vegetarian'), ('NO', 'None')], max_length=2),
            preserve_default=True,
        ),
    ]
