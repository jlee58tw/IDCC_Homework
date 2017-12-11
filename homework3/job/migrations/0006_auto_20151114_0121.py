# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0005_auto_20151114_0120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='jobname',
            field=models.CharField(max_length=20, blank=True),
        ),
    ]
