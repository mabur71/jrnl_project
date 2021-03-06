from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Sites(models.Model):
	name = models.CharField(max_length=20)
	printout = models.CharField(max_length=20)
	class Meta:
		db_table = 'sites'
	def __unicode__(self):
		return self.printout


class Records(models.Model):
	text = models.TextField()
	person = models.CharField(max_length=20)
	date = models.DateTimeField(auto_now_add=True)
	site = models.ForeignKey(Sites)
	class Meta:
		db_table = 'records'
		ordering = ['-id']

