# -*- coding: utf8 -*-
import re

from django import forms

class FlavourForm(forms.Form):
	name = forms.CharField(max_length=42)
	vcpu = forms.IntegerField()
	memory = forms.IntegerField()
	disk  = forms.IntegerField()

	def clean_name(self):
		name = self.cleaned_data['name']

		if not re.search(r'(^[a-zA-Z0-9ç_-])', name):
			raise forms.ValidationError('invalid characters')

		return name

class FlavourEditForm(forms.Form):
	vcpu = forms.IntegerField()
	memory = forms.IntegerField()
	disk  = forms.IntegerField()
