# -*- coding: utf8 -*-

from django import forms

class FlavourForm(forms.Form):
	name = forms.CharField(max_length=42)
	vcpu = forms.IntegerField()
	memory = forms.IntegerField()
	disk  = forms.IntegerField()

class FlavourEditForm(forms.Form):
	vcpu = forms.IntegerField()
	memory = forms.IntegerField()
	disk  = forms.IntegerField()
