# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import blog.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20150413_2010'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='recipes',
        ),
        migrations.AddField(
            model_name='recipe',
            name='post',
            field=models.ForeignKey(related_name='recipes', to='blog.Post', default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(upload_to=blog.models.random_file_path),
        ),
    ]
