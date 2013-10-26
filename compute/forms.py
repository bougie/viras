# -*- coding: utf8 -*-

from django import forms

class ComputeForm(forms.Form):
	name = forms.CharField(max_length=42)
	vcpu = forms.IntegerField()
	memory = forms.IntegerField()
	disk  = forms.IntegerField()
	ctype = forms.CharField(max_length=6)
