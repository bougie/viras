#-*- coding: utf8 -*-
import logging

from lib.exception import ErrorException
from lib.response import ErrorResponse, OkResponse, RedirectResponse

from django.http import HttpResponse, QueryDict
from django.utils import simplejson
from django.core.urlresolvers import reverse

from keystore.forms import ApiKeyForm, AuthForm
from keystore.utils import api_add, api_delete, api_get, api_get_all, consumer_delete, consumer_get, consumer_get_all

logger = logging.getLogger("app")

@required_auth_query
def api_index(request):
	if request.method == 'GET':
		response_data = {}

		try:
			data = api_get_all()
			
			response_data = {
				'count': len(data),
				'results': data
			}

			return OkResponse(200, data = response_data)
		except ErrorException, e:
			return ErrorResponse(status=e.code)
		except Exception, e:
			logger.error(str(e))
			return ErrorResponse(status=500)
	elif request.method == 'POST':
		form = ApiKeyForm(request.POST)
		
		if form.is_valid():
			try:
				aid = api_add(
					form.cleaned_data['name'],
					form.cleaned_data['decription'])

				return RedirectResponse(
					201,
					url = reverse('api_settings', args = {aid,})
				)
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
def api_settings(request, aid):
	if request.method == 'GET':
		response_data = {}

		try:
			data = api_get(aid)
			
			response_data = {
				'count': 1,
				'results': data
			}
			
			return OkResponse(200, data = response_data)
		except ErrorException, e:
			return ErrorResponse(status=e.code)
		except Exception, e:
			logger.error(str(e))
			return ErrorResponse(status=404)
	elif request.method == 'DELETE':
		try:
			api_delete(aid)

			return OkResponse(200)
		except ErrorException, e:
			return ErrorResponse(status=e.code)
		except Exception, e:
			logger.error(str(e))
			return ErrorResponse(status=500)
	else:
		return ErrorResponse(status=501)

@required_auth_query
def consumer_index(request):
	if request.method == 'GET':
		response_data = {}

		try:
			data = consumer_get_all()
			
			response_data = {
				'count': len(data),
				'results': data
			}
			return OkResponse(200, data = response_data)
		except ErrorException, e:
			return ErrorResponse(status=e.code)
		except Exception, e:
			logger.error(str(e))
			return ErrorResponse(status=500)
	else:
		return ErrorResponse(status=501)

@required_auth_query
def consumer_settings(request, cid):
	if request.method == 'GET':
		response_data = {}

		try:
			data = consumer_get(cid)

			response_data = {
				'count': 1,
				'results': data
			}
			return OkResponse(200, data = response_data)
		except ErrorException, e:
			return ErrorResponse(status=e.code)
		except Exception, e:
			logger.error(str(e))
			return ErrorResponse(status=404)
	elif request.method == 'DELETE':
		try:
			consumer_delete(cid)

			return OkResponse(200)
		except ErrorException, e:
			return ErrorResponse(status=e.code)
		except Exception, e:
			logger.error(str(e))
			return ErrorResponse(status=500)
	else:
		return ErrorResponse(status=501)
