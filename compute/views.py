#-*- coding: utf8 -*-

from django.http import HttpResponse, QueryDict
from django.utils import simplejson

from compute.forms import ComputeForm, ComputeEditForm
from compute.utils import add, delete, edit, get, get_all

def index(request):
	if request.method == 'GET':
		response_data = {}

		try:
			data = get_all()
			
			response_data = {
				'count': len(data),
				'results': data
			}
			return HttpResponse(simplejson.dumps(response_data), content_type="application/json")
		except:
			return HttpResponse(status=500)
	elif request.method == 'POST':
		form = ComputeForm(request.POST)

		if form.is_valid():
			try:
				add(
					form.cleaned_data['name'],
					form.cleaned_data['vcpu'],
					form.cleaned_data['memory'],
					form.cleaned_data['disk'],
					form.cleaned_data['ctype'])

				return HttpResponse(status=201)
			except:
				return HttpResponse(status=500)
		else:
			return HttpResponse(status=400)
	else:
		return HttpResponse(status=501)

def settings(request, cid):
	if request.method == 'GET':
		response_data = {}

		try:
			data = get(cid)
			
			response_data = {
				'count': len(data),
				'results': data
			}
			return HttpResponse(simplejson.dumps(response_data), content_type="application/json")
		except:
			return HttpResponse(status=404)
	elif request.method == 'PUT':
		params = QueryDict(request.body, request.encoding)
		form = ComputeEditForm(params)
		
		if form.is_valid():
			try:
				edit(
					cid,
					form.cleaned_data['vcpu'],
					form.cleaned_data['memory'],
					form.cleaned_data['disk'],
					form.cleaned_data['ctype'])

				return HttpResponse(status=200)
			except:
				return HttpResponse(status=500)
		else:
			return HttpResponse(status=400)
	elif request.method == 'DELETE':
		try:
			delete(cid)

			return HttpResponse(status=200)
		except:
			return HttpResponse(status=500)
	else:
		return HttpResponse(status=501)
