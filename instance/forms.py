# -*- coding: utf8 -*-
import re

from django import forms

class InstanceForm(forms.Form):
	name = forms.CharField(max_length=42)
	desc = forms.CharField(max_length=255, required=False)
	flavour = forms.CharField(max_length=42)

	def clean_name(self):
		name = self.cleaned_data['name']

		if not re.search(r'(^[a-zA-Z0-9ç_-])', name):
			raise forms.ValidationError('invalid characters')

		return name

class InstanceEditForm(forms.Form):
	desc = forms.CharField(max_length=255, required=False)
