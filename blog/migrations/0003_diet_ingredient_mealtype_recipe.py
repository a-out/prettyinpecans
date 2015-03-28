# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20150326_1751'),
    ]

    operations = [
        migrations.CreateModel(
            name='Diet',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(choices=[('DF', 'Dairy Free'), ('GF', 'Gluten Free'), ('RW', 'Raw'), ('VG', 'Vegan'), ('VT', 'Vegetarian')], max_length=2)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MealType',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=32)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('season', models.CharField(choices=[('SP', 'Spring'), ('SU', 'Summer'), ('FA', 'Fall'), ('WI', 'Winter')], max_length=2)),
                ('calories', models.IntegerField()),
                ('diets', models.ManyToManyField(to='blog.Diet')),
                ('ingredients', models.ManyToManyField(to='blog.Ingredient')),
                ('mealTypes', models.ManyToManyField(to='blog.MealType')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
