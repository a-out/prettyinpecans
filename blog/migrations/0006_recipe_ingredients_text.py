# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20150407_1528'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='ingredients_text',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
