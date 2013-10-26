# -*- coding: utf8 -*-

from django.db import models

class Compute(models.Model):
	name = models.CharField(max_length=42, unique=True)
	vcpu = models.IntegerField()
	memory = models.IntegerField()
	disk  = models.IntegerField()
	ctype = models.CharField(max_length=6)
