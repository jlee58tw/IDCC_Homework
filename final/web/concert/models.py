from __future__ import unicode_literals
from django.db import models

class Concert(models.Model):
    id = models.BigIntegerField(primary_key=True)
    uid = models.CharField(max_length=25)
    title = models.CharField(max_length=100)
    singer = models.CharField(max_length=30)
    singerid = models.IntegerField()
    process = models.IntegerField()
    start = models.DateTimeField()
    end = models.DateTimeField()
    web = models.CharField(max_length=150)
    webname = models.CharField(db_column='webName', max_length=20)  # Field name made lowercase.
    count = models.IntegerField()
    time = models.DateTimeField()
    location = models.CharField(max_length=100)
    locationname = models.CharField(db_column='locationName', max_length=100)  # Field name made lowercase.
    onsales = models.CharField(max_length=1)
    price = models.CharField(max_length=100)
    lat = models.CharField(max_length=20)
    lon = models.CharField(max_length=20)
    url_pic = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'concert'

class Ptt(models.Model):
    id = models.BigIntegerField(primary_key=True)
    postid = models.IntegerField()
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=30)
    time = models.DateTimeField()
    process = models.IntegerField()
    price = models.SmallIntegerField()
    num = models.SmallIntegerField()
    raw = models.TextField()
    url = models.CharField(max_length=100)
    singer = models.CharField(max_length=20)
    singerid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ptt'

class Singer(models.Model):
    active = models.IntegerField()
    id = models.BigIntegerField(primary_key=True)
    firstword = models.CharField(max_length=3)
    name = models.CharField(max_length=30)
    sex = models.IntegerField()
    region = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'singer'

class Subscribe(models.Model):
    userid = models.IntegerField()
    singerid = models.IntegerField()
    singername = models.CharField(max_length=30)
    email = models.CharField(max_length=40)
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'subscribe'
