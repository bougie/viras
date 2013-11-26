# -*- coding: utf8 -*-

from django.db import models
from django.contrib.auth.models import User

class ApiKey(models.Model):
	api_key = models.CharField(max_length=255, unique=True)
	api_secret = models.CharField(max_length=255, unique=True)
	name = models.CharField(max_length=255)
	description = models.CharField(max_length=255, blank=True, null=True)

class ConsumerKey(models.Model):
	consumer_key = models.CharField(max_length=255, unique=True)
	expiration = models.IntegerField(blank=True, null=True)

	user = models.ForeignKey(User)
