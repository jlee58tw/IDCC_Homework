# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import job.models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('file1', models.FileField(upload_to=job.models.upload_mapper, default='0')),
                ('file2', models.FileField(upload_to=job.models.upload_reducer, default='0')),
                ('file3', models.FileField(upload_to=job.models.upload_inputfile, default='0')),
                ('datetime', models.DateTimeField(null=True, blank=True)),
                ('jobname', models.CharField(max_length=20, default='default')),
                ('user', models.ForeignKey(default='0', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
