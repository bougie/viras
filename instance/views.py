#-*- coding: utf8 -*-

from django.http import HttpResponse, QueryDict
from django.utils import simplejson

from instance.forms import InstanceForm
from instance.utils import add

def index(request, cname):
	if request.method == 'GET':
		pass
	elif request.method == 'POST':
		form = InstanceForm(request.POST)

		if form.is_valid():
			uid = 1

			try:
				add(
					uid,
					cname,
					form.cleaned_data['name'],
					form.cleaned_data['desc'],
					form.cleaned_data['flavour'])

				return HttpResponse(status=201)
			except:
				return HttpResponse(status=500)
		else:
			return HttpResponse(status=400)
	else:
		return HttpResponse(status=501)

