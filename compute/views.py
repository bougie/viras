#-*- coding: utf8 -*-

from django.http import HttpResponse
from django.utils import simplejson

from compute.models import Compute
from compute.forms import ComputeForm

def index(request):
	if request.method == 'GET':
		response_data = {}
		data = []
		
		_data = Compute.objects.all()
		for d in _data:
			data.append({
				'id': d.id,
				'name': d.name,
				'vcpu': d.vcpu,
				'memory': d.memory,
				'disk': d.disk,
				'ctype': d.ctype
			})

		response_data = {
			'count': len(data),
			'results': data
		}
		return HttpResponse(simplejson.dumps(response_data), content_type="application/json")
	elif request.method == 'POST':
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

def change(request, cid):
	if request.method == 'DELETE':
		try:
			cte = Compute.objects.get(id=cid)
		except:
			return HttpResponse(status=400)

		try:
			cte.delete()

			return HttpResponse(status=200)
		except:
			return HttpResponse(status=500)
	else:
		return HttpResponse(status=501)
