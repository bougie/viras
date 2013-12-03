#-*- coding: utf8 -*-
import logging

from lib.exception import ErrorException
from lib.response import ErrorResponse, OkResponse

from django.http import QueryDict
from django.utils import simplejson

from auth.forms import AuthForm
from keystore.utils import api_exists, consumer_add

logger = logging.getLogger("app")

def authenticate(request):
	if request.method == 'POST':
		form = AuthForm(request.POST)

		if form.is_valid() and 'HTTP_X_VIRAS_APPLICATION' in request.META and 'HTTP_X_VIRAS_SECRET' in request.META:
			akey = request.META['HTTP_X_VIRAS_APPLICATION']
			asecret = request.META['HTTP_X_VIRAS_SECRET']

			if api_exists(akey, asecret):
				try:
					consumer_key = consumer_add(
						form.cleaned_data['login'],
						form.cleaned_data['password'])

					return OkResponse(status=201, data = {'consumer_key': consumer_key})
				except ErrorException, e:
					return ErrorResponse(status=e.code)
				except Exception, e:
					logger.error(str(e))
					return ErrorResponse(status=500)
			else:
				return ErrorResponse(status=403)
		else:
			return ErrorResponse(status=400)
	else:
		return ErrorResponse(status=501)
