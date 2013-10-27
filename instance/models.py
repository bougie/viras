#-*- coding: utf8 -*-

from django.db import models

from compute.models import Compute

class Instance(models.Model):
	uid = models.IntegerField()
	name = models.CharField(max_length=42, unique=True)
	desc = models.CharField(max_length=255, blank=True, null=True)
	vcpu = models.IntegerField()
	memory = models.IntegerField()
	disk  = models.IntegerField()
	state = models.IntegerField(blank=True, null=True)
	task = models.CharField(max_length=42, blank=True, null=True)
	power_state = models.IntegerField(blank=True, null=True)
	ipv4 = models.CharField(max_length=15, blank=True, null=True)
	ipv6 = models.CharField(max_length=40, blank=True, null=True)

	compute = models.ForeignKey(Compute)
