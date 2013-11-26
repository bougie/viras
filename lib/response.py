#-*- coding: utf8 -*-

from django.http import HttpResponse
from django.utils import simplejson

def ErrorResponse(status, message = '', message_code = 0):
	ret = {}

	if message != '':
		ret['message'] = message

	if message_code != 0:
		ret['message_code'] = message_code

	return HttpResponse(
		simplejson.dumps(ret),
		status=status,
		content_type="application/json")

def OkResponse(status, data = {}):
	return HttpResponse(
		simplejson.dumps(data),
		status=status,
		content_type="application/json")

def RedirectResponse(status, url):
	data = {
		'Location': url
	}

	resp = HttpResponse(
		simplejson.dumps(data),
		status=status,
		content_type="application/json")

	resp['Location'] = url;

	return resp
