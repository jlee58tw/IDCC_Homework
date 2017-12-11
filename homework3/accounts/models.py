from django.db import models
from django.contrib.auth.models import User

class Userid(models.Model):
	id = models.AutoField(primary_key=True)
	user = models.ForeignKey(User, default='0')