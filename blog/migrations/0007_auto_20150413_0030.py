# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_recipe_ingredients_text'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='mealTypes',
        ),
        migrations.AddField(
            model_name='recipe',
            name='meal_type',
            field=models.ForeignKey(default=None, to='blog.MealType'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='recipes',
            field=models.ManyToManyField(related_name='posts', to='blog.Recipe'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='ingredients',
            field=models.ManyToManyField(related_name='recipes', to='blog.Ingredient'),
        ),
    ]
