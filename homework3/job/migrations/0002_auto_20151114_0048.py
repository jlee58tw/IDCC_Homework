# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='file1',
        ),
        migrations.RemoveField(
            model_name='document',
            name='file2',
        ),
        migrations.RemoveField(
            model_name='document',
            name='file3',
        ),
    ]
