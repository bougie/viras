#-*- coding: utf8 -*-
import logging

from lib.exception import ErrorException
from lib.response import ErrorResponse

from django.http import HttpResponse, QueryDict
from django.utils import simplejson

from flavour.forms import FlavourForm, FlavourEditForm
from flavour.utils import add, delete, edit, get, get_all
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
		form = FlavourForm(request.POST)

		if form.is_valid():
			try:
				add(
					form.cleaned_data['name'],
					form.cleaned_data['vcpu'],
					form.cleaned_data['memory'],
					form.cleaned_data['disk'])

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
def settings(request, fid):
	if request.method == 'GET':
		response_data = {}

		try:
			data = get(fid)
			
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
		form = FlavourEditForm(params)
		
		if form.is_valid():
			try:
				edit(
					fid,
					form.cleaned_data['vcpu'],
					form.cleaned_data['memory'],
					form.cleaned_data['disk'])

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
			delete(fid)

			return HttpResponse(status=200)
		except ErrorException, e:
			return ErrorResponse(status=e.code)
		except Exception, e:
			logger.error(str(e))
			return ErrorResponse(status=500)
	else:
		return ErrorResponse(status=501)
