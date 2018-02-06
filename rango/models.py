from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Category(models.Model):
	name=models.CharField(max_length=128, unique=True)
	class Meta:
		verbose_name_plural='Categories'
	
	def _str_(self):
		return self.name
	def _unicode_(self):
		return self.name

class Page(models.Model):
	category=models.ForeignKey(Category)
	title=models.CharField(max_length=128)
	url=models.URLField()
	views=models.IntegerField(default=0)
	def _str_(self):
		return self.title
	def _unicode_(self):
		return self.title
