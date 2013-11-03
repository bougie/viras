# -*- coding: utf8 -*-

import re

from django import forms

class ComputeForm(forms.Form):
	name = forms.CharField(max_length=42)
	vcpu = forms.IntegerField()
	memory = forms.IntegerField()
	disk  = forms.IntegerField()
	ctype = forms.CharField(max_length=6)

	def clean_name(self):
		name = self.cleaned_data['name']

		if not re.search(r'(^[a-zA-Z0-9ç_-])', name):
			raise forms.ValidationError('invalid characters')

		return name

class ComputeEditForm(forms.Form):
	vcpu = forms.IntegerField()
	memory = forms.IntegerField()
	disk  = forms.IntegerField()
	ctype = forms.CharField(max_length=6)
