#-*- coding: utf8 -*-
import logging

from lib.exception import ErrorException
from lib.response import ErrorResponse

from django.http import HttpResponse, QueryDict
from django.utils import simplejson

from compute.forms import ComputeForm, ComputeEditForm, ComputeIpRangeForm
from compute.utils import add, delete, edit, get, get_obj, get_all, add_range_ips
from auth.decorators import required_auth_query

logger = logging.getLogger("app")

@required_auth_query
def index(request):
	if request.method == 'GET':
		response_data = {}

		try:
			data = get_all()
			
			response_data = {
				'count': len(data),
				'results': data
			}
			return HttpResponse(
				simplejson.dumps(response_data),
				content_type="application/json")
		except ErrorException, e:
			return ErrorResponse(status=e.code)
		except Exception, e:
			logger.error(str(e))
			return ErrorResponse(status=500)
	elif request.method == 'POST':
		form = ComputeForm(request.POST)

		if form.is_valid():
			try:
				add(
					form.cleaned_data['name'],
					form.cleaned_data['vcpu'],
					form.cleaned_data['memory'],
					form.cleaned_data['disk'],
					form.cleaned_data['ctype'],
					form.cleaned_data['ipv4'],
					form.cleaned_data['ipv6'])

				return HttpResponse(status=201)
			except ErrorException, e:
				return ErrorResponse(status=e.code)
			except Exception, e:
				logger.error(str(e))
				return ErrorResponse(status=500)
		else:
			return ErrorResponse(status=400)
	else:
		return ErrorResponse(status=501)

@required_auth_query
def settings(request, cid):
	if request.method == 'GET':
		response_data = {}

		try:
			data = get(cid)
			
			response_data = {
				'count': 1,
				'results': data
			}
			return HttpResponse(
				simplejson.dumps(response_data),
				content_type="application/json")
		except ErrorException, e:
			return ErrorResponse(status=e.code)
		except Exception, e:
			logger.error(str(e))
			return ErrorResponse(status=404)
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
					form.cleaned_data['ctype'],
					form.cleaned_data['ipv4'],
					form.cleaned_data['ipv6'])

				return HttpResponse(status=200)
			except ErrorException, e:
				return ErrorResponse(status=e.code)
			except Exception, e:
				logger.error(str(e))
				return ErrorResponse(status=500)
		else:
			return ErrorResponse(status=400)
	elif request.method == 'DELETE':
		try:
			delete(cid)

			return HttpResponse(status=200)
		except ErrorException, e:
			return ErrorResponse(status=e.code)
		except Exception, e:
			logger.error(str(e))
			return ErrorResponse(status=500)
	else:
		return ErrorResponse(status=501)

@required_auth_query
def ip(request, cname):
	if request.method == 'GET':
		pass
	elif request.method == 'POST':
		form = ComputeIpRangeForm(request.POST)

		if form.is_valid():
			try:
				compute = get_obj(name=name)
			except ErrorException, e:
				return ErrorResponse(status=e.code)

			try:
				add_range_ips(
					compute,
					form.cleaned_data['range_min'],
					form.cleaned_data['range_max'],
					form.cleaned_data['range_mask'],
					form.cleaned_data['mask'])

				return HttpResponse(status=201)
			except ErrorException, e:
				return ErrorResponse(status=e.code)
			except Exception, e:
				logger.error(str(e))
				return ErrorResponse(status=500)
		else:
			return ErrorResponse(status=400)

@required_auth_query
def ip_settings(request, cid):
	if request.method == 'GET':
		pass
	elif request.method == 'PUT':
		pass
	elif request.method == 'DELETE':
		pass
