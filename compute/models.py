# -*- coding: utf8 -*-

from django.db import models

class Compute(models.Model):
	name = models.CharField(max_length=42, unique=True)
	vcpu = models.IntegerField()
	memory = models.IntegerField()
	disk  = models.IntegerField()
	ctype = models.CharField(max_length=6)
	ipv4 = models.CharField(max_length=15, blank=True, null=True)
	ipv6 = models.CharField(max_length=40, blank=True, null=True)

class ComputesIps(models.Model):
	range_min = models.CharField(max_length=15)
	range_max = models.CharField(max_length=15)
	range_mask = models.Charfield(max_length=15)
	mask = models.Charfield(max_length=15)

	compute = models.ForeignKey(Compute)
