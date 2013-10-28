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
