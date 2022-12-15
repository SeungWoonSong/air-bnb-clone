from statistics import mode
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class House(models.Model):
	# 모델을 상속하는중
	"""Model Definition For House"""
	name = models.CharField(max_length = 140)
	price_per_night = models.PositiveBigIntegerField()
	description = models.TextField()
	address = models.CharField(max_length = 140)
	pets_allowed = models.BooleanField(default = True, help_text = "Is This house Allow Pets?")

	def __str__(self):
		return self.name