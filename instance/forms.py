# -*- coding: utf8 -*-

from django import forms

class InstanceForm(forms.Form):
	name = forms.CharField(max_length=42)
	desc = forms.CharField(max_length=255, required=False)
	flavour = forms.CharField(max_length=42)

class InstanceEditForm(forms.Form):
	desc = forms.CharField(max_length=255, required=False)
