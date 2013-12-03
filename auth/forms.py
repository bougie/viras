# -*- coding: utf8 -*-

from django import forms

class AuthForm(forms.Form):
	login = forms.CharField(max_length=255)
	password = forms.CharField(max_length=255)
