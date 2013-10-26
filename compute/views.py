#-*- coding: utf8 -*-

from django.http import HttpResponse
from django.utils import simplejson

from compute.models import Compute
from compute.forms import ComputeForm

def index(request):
	if request.method == 'GET':
		response_data = {}

		data = Compute.objects.all()
		if len(data) == 0:
			data = ['']

		response_data = {
			"results": data
		}
		return HttpResponse(simplejson.dumps(response_data), content_type="application/json")
	else:
		return HttpResponse(status=501)

def add(request):
	if request.method == 'POST':
		form = ComputeForm(request.POST)

		if form.is_valid():
			cte = Compute()

			cte.name = form.cleaned_data['name']
			cte.vcpu = form.cleaned_data['vcpu']
			cte.memory = form.cleaned_data['memory']
			cte.disk = form.cleaned_data['disk']
			cte.ctype = form.cleaned_data['ctype']

			try:
				cte.save()

				return HttpResponse(status=200)
			except:
				return HttpResponse(status=500)
		else:
			return HttpResponse(status=400)
	else:
		return HttpResponse(status=501)
