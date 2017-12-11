# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('concert', '0002_delete_concert'),
    ]

    operations = [
        migrations.CreateModel(
            name='Concert',
            fields=[
                ('id', models.BigIntegerField(serialize=False, primary_key=True)),
                ('uid', models.CharField(max_length=25)),
                ('title', models.CharField(max_length=100)),
                ('singer', models.CharField(max_length=30)),
                ('start', models.DateTimeField()),
                ('end', models.DateTimeField()),
                ('web', models.CharField(max_length=150)),
                ('webname', models.CharField(max_length=20, db_column='webName')),
                ('count', models.IntegerField()),
                ('time', models.DateTimeField()),
                ('location', models.CharField(max_length=100)),
                ('locationname', models.CharField(max_length=100, db_column='locationName')),
                ('onsales', models.CharField(max_length=1)),
                ('price', models.CharField(max_length=100)),
                ('lat', models.CharField(max_length=20)),
                ('lon', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'concert',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Ptt',
            fields=[
                ('id', models.BigIntegerField(serialize=False, primary_key=True)),
                ('postid', models.IntegerField()),
                ('title', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=30)),
                ('time', models.DateTimeField()),
                ('process', models.IntegerField()),
                ('price', models.SmallIntegerField()),
                ('num', models.SmallIntegerField()),
                ('raw', models.TextField()),
                ('url', models.CharField(max_length=100)),
                ('singer', models.CharField(max_length=20)),
                ('singerid', models.IntegerField()),
            ],
            options={
                'db_table': 'ptt',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Singer',
            fields=[
                ('active', models.IntegerField()),
                ('id', models.BigIntegerField(serialize=False, primary_key=True)),
                ('firstword', models.CharField(max_length=3)),
                ('name', models.CharField(max_length=30)),
                ('sex', models.IntegerField()),
                ('region', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'singer',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Subscribe',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('userid', models.IntegerField()),
                ('singerid', models.IntegerField()),
                ('singername', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=40)),
                ('time', models.DateTimeField()),
            ],
            options={
                'db_table': 'subscribe',
                'managed': False,
            },
        ),
    ]
