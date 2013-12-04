# -*- coding: utf8 -*-

import re

from django import forms

class ComputeForm(forms.Form):
	name = forms.CharField(max_length=42)
	vcpu = forms.IntegerField()
	memory = forms.IntegerField()
	disk  = forms.IntegerField()
	ctype = forms.CharField(max_length=6)
	ipv4 = forms.CharField(max_length=10, required=False)
	ipv6 = forms.CharField(max_length=50, required=False)

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
	ipv4 = forms.CharField(max_length=10, required=False)
	ipv6 = forms.CharField(max_length=50, required=False)

class ComputeIpRangeForm(forms.Form):
	range_min = forms.CharField(max_length=15)
	range_max = forms.CharField(max_length=15)
	range_mask = forms.CharField(max_length=15)
	mask = forms.CharField(max_length=15)
