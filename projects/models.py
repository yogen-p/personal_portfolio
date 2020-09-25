from django.db import models

class Projects(models.Model):
	"""Defining database Model"""
	title = models.CharField(max_length=128)
	description = models.TextField()
	technology = models.CharField(max_length=32)
	url = models.CharField(max_length=128)
	image = models.FilePathField(path="/img")
		
