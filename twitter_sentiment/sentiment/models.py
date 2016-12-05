from __future__ import unicode_literals

from django.db import models

class TwitterSentiment(models.Model):
	username	=models.CharField(max_length=200)
	text 		=models.TextField()
	sentiment   =models.CharField(max_length=100)

	def __unicode__(self):
		return self.sentiment


