# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20150416_1403'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='type',
            field=models.CharField(default='FOOD', max_length=16, choices=[('FOOD', 'Food'), ('FASHION', 'Fashion'), ('TRAVEL', 'Travel')]),
            preserve_default=False,
        ),
    ]
