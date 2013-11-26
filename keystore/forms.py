# -*- coding: utf8 -*-

from django import forms

class ApiKeyForm(forms.Form):
	name = forms.CharField(max_length=255)
	decription = forms.CharField(max_length=255, required=False)

class AuthForm(forms.Form):
	api_key = forms.CharField(max_length=255)
	api_secret = forms.CharField(max_length=255)
	login = forms.CharField(max_length=255)
	password = forms.CharField(max_length=255)
