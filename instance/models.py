#-*- coding: utf8 -*-

from django.db import models

from compute.models import Compute

class Instance(models.Model):
	name = models.CharField(max_length=42, unique=True)
	vcpu = models.IntegerField()
	memory = models.IntegerField()
	disk  = models.IntegerField()
	state = models.IntegerField()
	task = models.CharField(max_length=42, blank=True)
	power_state = models.IntegerField(, blank=True)
	ipv4 = models.CharField(max_length=15, blank=True)
	ipv6 = models.CharField(max_length=40, blank=True)

	compute = models.ForeignKey(Compute)
