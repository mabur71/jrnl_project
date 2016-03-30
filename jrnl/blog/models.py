from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Site(models.Model):
	name = models.CharField(max_length=20)
	class Meta:
		db_table = 'sites'


class Records(models.Model):
	text = models.TextField()
	person = models.CharField(max_length=20)
	date = models.DateTimeField(auto_now_add=True)
	site = models.ForeignKey(Site)
	class Meta:
		db_table = 'records'
		ordering = ['-id']

