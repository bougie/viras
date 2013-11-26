#-*- coding: utf8 -*-
import logging

from lib.exception import ErrorException
from lib.response import ErrorResponse

from django.http import HttpResponse, QueryDict
from django.utils import simplejson

from instance.forms import InstanceForm, InstanceEditForm
from instance.utils import add, edit, get, get_all_by_compute

logger = logging.getLogger("app")

@required_auth_query
def index(request, cname):
	if request.method == 'GET':
		response_data = {}

		uid = 1

		try:
			data = get_all_by_compute(cname, uid)
			
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
def settings(request, cname, iname):
	if request.method == 'GET':
		try:
			ins = get(cname, iname)

			response_data = {
				'count': 1,
				'results': ins
			}
			return HttpResponse(
				simplejson.dumps(response_data),
				content_type="application/json")
		except ErrorException, e:
			return ErrorResponse(status=e.code)
		except Exception, e:
			logger.error(str(e))
			return ErrorResponse(status=500)
	elif request.method == 'PUT':
		params = QueryDict(request.body, request.encoding)
		form = InstanceEditForm(params)

		if form.is_valid():
			try:
				edit(
					cname,
					iname,
					form.cleaned_data['desc'])

				return HttpResponse(status=200)
			except ErrorException, e:
				return ErrorResponse(status=e.code)
			except Exception, e:
				logger.error(str(e))
				return ErrorResponse(status=500)
		else:
			return ErrorResponse(status=400)
	else:
		return ErrorResponse(status=501)
