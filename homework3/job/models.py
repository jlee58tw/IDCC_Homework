# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from accounts.models import Userid


def upload_mapper(self, filename):
	#uid = Userid.objects.get(username=self.user.username)
    return '/'.join([str(self.user.id), "mapper.py"])

def upload_reducer(self, filename):
	#uid = Userid.objects.get(username=self.user.username)
    return '/'.join([str(self.user.id), "reducer.py"])
	
def upload_inputfile(self, filename):
	#uid = Userid.objects.get(username=self.user.username)
    return '/'.join([str(self.user.id), "input.txt"])

class Document(models.Model):

	id = models.AutoField(primary_key=True)
	#file1 = models.FileField(upload_to=upload_mapper, default='0')
	#file2 = models.FileField(upload_to=upload_reducer, default='0')
	#file3 = models.FileField(upload_to=upload_inputfile, default='0')
	datetime = models.DateTimeField(null=True, blank=True)
	user = models.ForeignKey(User, blank=True)
	status = models.CharField(max_length=10, null=True, blank=True)
	jobname = models.CharField(max_length=20, null=True, blank=True)